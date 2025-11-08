import random
from class_exercises_.OOP.FightingFantasy import Character, PC, Game

'''
This is the file where i'm going to be creating the CLI for the game :P'''

'''
This is Olfana! A land in a world unlike our own!!
The people of Olfana are frightened by the threat of demons called Necrosofia
Necrosofia possess a mysterious power called mind and are plotting to conquer Olfana and enact their fiendish limited edition plot
In order to stop this plan, the King formed a group of br'''


class GameCLI:

    def __init__(self):
        self.game = Game()
        self.run_game()

    def run_game(self):

        # INTRO
        print("-" * 100)
        print("Greetings traveller and welcome to Olfana!!")
        print("-" * 100)
        print("This here tale takes place in a magical land of curious creatures and" + "\n" +
              "fantastical fables called Olfana! A land in a world unlike our own!!!" + "\n" +
              "(No. This is not plagarism...)" + "\n" + "\n" +
              "The people of Olfana are frightened by the threat of a growing group" + "\n" +
              "called Necrosofia, which contains members from all the most dangerous" + "\n" +
              "species in the realm. Necrosofia possess numerous mysterious powers yet" + "\n" +
              "undisclosed to the public and to be discovered and destroyed during" + "\n" +
              "battle, perhaps even claimed as your own. With these, they intend to " + "\n" +
              "enact their fiendish limited edition plot and conquer Olfana as their own!")
        print("-" * 100)

        # CREATING CHARACTER
        start = input("Traveller! Will you lead our campaign and decimate out enemies? [y/n] ")

        if start.lower() != "y":
            print()
            print("Traveller, unfortunately you have no choice! As you have been anointed" + "\n" +
                  "by the king, it is your regal duty and honor to agree, or face cruel" + "\n" +
                  "punishment and dishonor the sword itself.")
            print()

        name = input("Proclaim your title for this quest: ")
        pc = PC.generate_player_character(name)

        print("-" * 100)
        print(f"Good {pc.name}, thankest thou for embarking upon this mission! Thine" + "\n" +
              "statistics are as follows:\n")
        print(pc) #TODO need to fix this

    def fight_opponent(self):
        pass

    def fight_battle(self):
        pass

if __name__ == "__main__":
    GameCLI()