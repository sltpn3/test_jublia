from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from model.base import Base


class EmailToSend(Base):
    __tablename__ = 'email_to_send'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    email_subject = Column(String(256, collation='utf8mb4_general_ci'))
    email_content = Column(Text(collation='utf8mb4_general_ci'))
    timestamp = Column(TIMESTAMP)

    event = relationship('Event')
