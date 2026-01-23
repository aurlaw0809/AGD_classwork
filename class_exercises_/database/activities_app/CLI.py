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
        participants = self.controller.get_person_activities(activity)
        for participant in participants:
            print(participant)


if __name__ == '__main__':
    cli = CLI()

'''
cli.show_activities_persons()
Gang gang.
'''