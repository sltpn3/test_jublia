from model import email_to_send, email_event, email, event
from ConfigParser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText

import beanstalkc
import smtplib
import argparse


class SendEmail():

    def __init__(self, config_file='config.conf'):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)
        engine_config = 'mysql://{}:{}@{}/{}?charset=utf8mb4'.format(self.config.get('database', 'user'),
                                                                     self.config.get('database', 'pass'),
                                                                     self.config.get('database', 'host'),
                                                                     self.config.get('database', 'name'))
        self.engine = create_engine(engine_config)

    def job_pusher(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
        beans = beanstalkc.Connection(self.config.get('beanstalk', 'host'))
        beans.connect()
        beans.use('send_email')
        for a, b, c in session.query(email_to_send.EmailToSend, email.Email, email_event.EmailEvent)\
                .filter(email_to_send.EmailToSend.timestamp == now)\
                .filter(email_to_send.EmailToSend.event_id == email_event.EmailEvent.event_id)\
                .filter(email_event.EmailEvent.email_id == email.Email.id)\
                .all():
            job = '{}|{}'.format(a.id, b.email)
            print job
            beans.put(job, ttr=3600)

    def job_worker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        beans = beanstalkc.Connection(self.config.get('beanstalk', 'host'))
        beans.connect()
        beans.watch('send_email')
        run = True

        self._from = self.config.get('smtp', 'user')
        self.smtp = smtplib.SMTP_SSL(self.config.get('smtp', 'host'), self.config.get('smtp', 'port'))
        self.smtp.login(self._from, self.config.get('smtp', 'pass'))

        while run:
            job = beans.reserve()
            data = job.body.split('|')
            try:
                mail_to_send = session.query(email_to_send.EmailToSend)\
                    .filter(email_to_send.EmailToSend.id == data[0])\
                    .one()
                self.send_email(mail_to_send.email_subject, data[1], mail_to_send.email_content)
                job.delete()
            except Exception, e:
                print e
                job.bury()

    def send_email(self, subject, to_address, content):
        message = MIMEMultipart('alternative')
        message['From'] = self._from
        message['To'] = to_address
        message['Subject'] = subject
        message.attach(MIMEText(content.encode('utf8'), 'plain', 'utf-8'))
        self.smtp.sendmail(self._from, to_address, message.as_string())


if __name__ == '__main__':
    modes = ['pusher', 'worker']
    argparser = argparse.ArgumentParser(description='Send Email Engine',
                                        formatter_class=argparse.RawDescriptionHelpFormatter)
    argparser.add_argument('-m', '--mode', help='Mode: {}'.format(', '.join(modes)), metavar='',
                           default=None, type=str)
    argparser.add_argument('-c', '--config', help='Config File', metavar='', default='config.conf', type=str)

    args = argparser.parse_args()
    send_mail = SendEmail(args.config)

    if args.mode == "pusher":
        send_mail.job_pusher()
    elif args.mode == "worker":
        send_mail.job_worker()
