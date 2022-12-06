#!/usr/bin/python3
""" class definition of a State and an instance Base = declarative_base(): """

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format("root",
                                                            "All3gr3tto!",
                                                            "my_db"),
                pool_pre_ping=True)
    
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, nullable = False, primary_key = True, unique = true)
