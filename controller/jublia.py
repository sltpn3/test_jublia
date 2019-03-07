from ConfigParser import ConfigParser
from model import email_to_send, base, email, event, email_event
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
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def post_save_emails(self, event_id, email_subject, email_content, timestamp):
        email_content = email_content.encode('utf-8')
        mail = email_to_send.EmailToSend(event_id=event_id, email_subject=email_subject, email_content=email_content,
                                         timestamp=timestamp)
        self.session.add(mail)
        self.session.commit()

    def post_emails(self, email_address):
        e_mail = email.Email(email=email_address)
        self.session.add(e_mail)
        self.session.commit()

    def post_events(self, event_name):
        new_event = event.Event(event_name=event_name)
        self.session.add(new_event)
        self.session.commit()

    def post_email_events(self, email_id, event_id):
        new_email_event = email_event.EmailEvent(event_id=event_id, email_id=email_id)
        self.session.add(new_email_event)
        self.session.commit()

    def event_id_choices(self):
        return [(e.id, e.event_name) for e in self.session.query(event.Event).order_by('event_name')]

    def email_id_choices(self):
        return [(e.id, e.email) for e in self.session.query(email.Email).order_by('email')]
