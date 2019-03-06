from model.base import Base
from sqlalchemy import Column, Integer, String


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    email = Column(String(256))
