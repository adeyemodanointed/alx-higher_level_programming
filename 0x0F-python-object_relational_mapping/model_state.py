#!/usr/bin/python3
""" class definition of a State and an instance Base = declarative_base(): """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Define a class State to be linked to table"""

    __tablename__ = 'states'

    id = Column(Integer,
                nullable=False, primary_key=True,
                unique=True, autoincrement=True)

    name = Column(String(128), nullable=False)
