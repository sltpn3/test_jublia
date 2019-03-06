from model.base import Base
from sqlalchemy import Column, Integer, String


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True)
