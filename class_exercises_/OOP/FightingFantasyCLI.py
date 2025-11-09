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
        print("\nGREETINGS TRAVELLER, AND WELCOME TO OLFANA!!\n")
        print("-" * 100)
        print("\nThis here tale takes place in a magical land of curious creatures and" + "\n" +
              "fantastical fables called Olfana! A land in a world unlike our own!!!" + "\n" +
              "(No. This is not plagarism...)" + "\n" + "\n" +
              "The people of Olfana are frightened by the threat of a growing group" + "\n" +
              "called Necrosofia, which contains members from all the most dangerous" + "\n" +
              "species in the realm. Necrosofia possess numerous mysterious powers yet" + "\n" +
              "undisclosed to the public and to be discovered and destroyed during" + "\n" +
              "battle, perhaps even claimed as your own. With these, they intend to " + "\n" +
              "enact their fiendish limited edition plot and conquer Olfana as their own!\n")
        print("-" * 100)

        # CREATING CHARACTER
        start = input("\nTraveller! Will you lead our campaign and decimate out enemies? [y/n] ")

        if start.lower() != "y":
            print("\nTraveller, unfortunately you have no choice! As you have been anointed" + "\n" +
                  "by the king, it is your regal duty and honor to agree, or face cruel" + "\n" +
                  "punishment and dishonor the sword itself.\n")

        name = input("Proclaim your title for this quest: ")
        print()
        pc = PC.generate_player_character(name)
        self.game.set_player(pc)

        print("-" * 100)
        print(f"\nGood {pc.name}, thankest thou for embarking upon this mission! Thine" + "\n" +
              "statistics are as follows:\n")
        pc.return_stats()
        print("\nTake care to remember that statistics can increase or decrease" + "\n" +
              "during your mission. Fighting foes and losing will result in a" + "\n" +
              "decrease in stamina, while winning battles can help to increase" + "\n" +
              "your skill and prepare for the final boss! Half finishing fights" + "\n" +
              "with monsters may decrease your stamina but will result in no" + "\n" +
              "skill upgrades, keep this in mind when deciding to flee."+ "\n" + "\n" +
              "The final battle will be unlocked whenever your skill level passes" + "\n" +
              "the 20 point mark. Until then, you must prepare..." + "\n" + "\n" +
              f"Good luck {pc.name}!" + "\n")
        print("-" * 100)

    def fight_opponent(self):
        pass

    def fight_battle(self):
        pass

if __name__ == "__main__":
    GameCLI()