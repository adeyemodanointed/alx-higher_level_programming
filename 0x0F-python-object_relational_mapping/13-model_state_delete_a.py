#!/usr/bin/python3
""" deletes all State objects with a name containing the letter a"""
if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(argv[1],
                        argv[2],
                        argv[3]),
                pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session=False)
    session.commit()
