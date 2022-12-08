#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa """
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

    session.add(State(name='Louisiana'))
    for state in session.query(State).filter(State.name == 'Louisiana'):
        print('{}'.format(state.id))
    session.commit()
