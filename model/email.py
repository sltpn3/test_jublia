from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP

Base = declarative_base()


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    email_subject = Column(String(256))
    email_content = Column(Text)
    timestamp = Column(TIMESTAMP)

