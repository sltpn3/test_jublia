from ConfigParser import ConfigParser
from model import email_to_send, base, email, event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class JubliaController():

    def __init__(self, config_file='config.conf'):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)
        engine_config = 'mysql://{}:{}@{}/{}?charset=utf8mb4'.format(self.config.get('database', 'user'),
                                                                     self.config.get('database', 'pass'),
                                                                     self.config.get('database', 'host'),
                                                                     self.config.get('database', 'name'))
        self.engine = create_engine(engine_config)

    def post_save_emails(self, event_id, email_subject, email_content, timestamp):
        Session = sessionmaker(bind=self.engine)
        session = Session()
#         print email_content
        email_content = email_content.encode('utf-8')
#         print email_content
        mail = email_to_send.EmailToSend(event_id=event_id, email_subject=email_subject, email_content=email_content,
                                         timestamp=timestamp)
        session.add(mail)
        session.commit()
