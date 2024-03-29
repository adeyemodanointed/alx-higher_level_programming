#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """

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

    state = session.query(State).first()
    if(state):
        print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
