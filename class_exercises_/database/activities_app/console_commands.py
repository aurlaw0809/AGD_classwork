from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Person

# Connect to the activities database
engine = create_engine('sqlite:///activities.sqlite', echo=True)

'''
sess = Session(engine)
stmt = select(Person)
people = sess.scalars(stmt).all()

sess.commit
'''