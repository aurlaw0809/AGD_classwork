import sqlalchemy as sa
import sqlalchemy.orm as so

from models import Person, Activity

class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)

    def get_person_activities(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            user = session.scalar(stmt)
            activities = user.activities
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_activities_people(self, activity_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == activity_name)
            activity = session.scalar(stmt)
            peoples = activity.attendees
            people_names = [{person.first_name, person.last_name} for person in peoples]
        return people_names
    '''
    def get_all_people(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).order_by(Person.first_name)
            peoples = session.scalar(stmt)
            #TODO not working
            #person_names =[{person.first_name, person.last_name} for person in peoples]
        return peoples

    def get_all_activities(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity.name).order_by(Activity.name)
            activities = session.execute(stmt)
            print(activities)
            return activities
    '''

    def add_person(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            person = Person(first_name=first_name, last_name=last_name)
            session.add(person)
            session.commit()

    def delete_person(self, person_id):
        with so.Session(bind=self.engine) as session:
            person = session.get(Person, person_id)
            session.delete(person)
            session.commit()

    def add_activity(self, activity_name):
        with so.Session(bind=self.engine) as session:
            activity = Activity(name=activity_name)
            session.add(activity)
            session.commit()

    def delete_activity(self, activity_id):
        with so.Session(bind=self.engine) as session:
            activity = session.get(Activity, activity_id)
            session.delete(activity)
            session.commit()

    def edit_person_name(self, first_name, last_name, new_first_name, new_last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            person = session.scalar(stmt)
            person.first_name = new_first_name
            person.last_name = new_last_name
            session.commit()

    def delete_person_activity(self, person_id, activity_id):
        with so.Session(bind=self.engine) as session:
            activity = session.get(Activity, activity_id)
            person = session.get(Person, person_id)
            #TODO

    def add_person_activity(self, first_name, last_name, activity_id):
        pass


if __name__ == '__main__':
    controller = Controller()