# import pyinputplus as pyip

from controller import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)
        for activity in activities:
            print(activity)

    def show_activities_persons(self):
        activity = input('Enter activity: ')
        participants = self.controller.get_activities_people(activity)
        for participant in participants:
            print(participant)
    '''
    def show_all_people(self):
        people = self.controller.get_all_people()
        for person in people:
            print(person)

    def show_all_activities(self):
        activities = self.controller.get_all_activities()
        for activity in activities:
            print(activity)
    '''

    def add_person(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        self.controller.add_person(first_name, last_name)

    def delete_person(self):
        person_id = input('Enter person ID: ')
        self.controller.delete_person(person_id)

    def add_activity(self):
        name = input('Enter activity name: ')
        self.controller.add_activity(name)

    def delete_activity(self):
        activity_id = input('Enter activity ID: ')
        self.controller.delete_activity(activity_id)

    def edit_person_name(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        new_first_name = input('Enter new first name: ')
        new_last_name = input('Enter new last name: ')
        self.controller.edit_person(first_name, last_name, new_first_name, new_last_name)

    def delete_person_activity(self):
        person_id = input('Enter person ID: ')
        activity_id = input('Enter activity ID: ')
        self.controller.delete_person_activity(person_id, activity_id)

    def add_person_activity(self):
        person_id = input('Enter person ID: ')
        activity_id = input('Enter activity ID: ')
        self.controller.add_person_activity(person_id, activity_id)

    def edit_activity(self):
        pass


if __name__ == '__main__':
    cli = CLI()

'''
cli.show_activities_persons()
Gang gang.
cli.show_all_people()
'''