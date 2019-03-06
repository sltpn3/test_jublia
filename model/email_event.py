from model.base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class EmailEvent(Base):
    __tablename__ = 'email_event'
    email_id = Column(Integer, ForeignKey('email.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'), primary_key=True)

    event = relationship('Event')
    event = relationship('Email')
