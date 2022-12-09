#!/usr/bin/python3

"""
    prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from model_city import Base, City
    from model_state import Base, State
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()
    for state, city in res:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
