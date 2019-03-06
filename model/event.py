from model.base import Base
from sqlalchemy import Column, Integer, String


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    event_name = Column(String(256))
