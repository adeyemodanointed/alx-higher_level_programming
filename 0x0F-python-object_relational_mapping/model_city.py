#!/usr/bin/python3
""" class definition of a State and an instance Base = declarative_base(): """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
Base = declarative_base()


class City(Base):
    """Define a class City to be linked to table"""

    __tablename__ = 'cities'

    id = Column(Integer,
                nullable=False, primary_key=True,
                unique=True, autoincrement=True)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
