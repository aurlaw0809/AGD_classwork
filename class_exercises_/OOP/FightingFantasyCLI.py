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

        #CREATING GAME ------------------------------------------------------------------------
        #initialises variables and starts the game

        self.game = Game()
        self.run_game()

    def run_game(self):

        #INTRO --------------------------------------------------------------------------------
        #welcomes the player to the game and gives a brief background

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

        #CREATING CHARACTER -------------------------------------------------------------------
        #creates the character and returns statistics while giving some more background

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
        self.game.player.return_stats()
        print("\nTake care to remember that statistics can increase or decrease" + "\n" +
              "during your mission. Fighting foes and losing will result in a" + "\n" +
              "decrease in stamina, while winning battles can help to increase" + "\n" +
              "your skill and prepare for the final boss! Half finishing fights" + "\n" +
              "with monsters may decrease your stamina but will result in no" + "\n" +
              "skill upgrades, keep this in mind when deciding to flee. You will"+ "\n" +
              "also not receive the chance to fight the same monster again, which" + "\n" +
              "could result in a lower or insufficient skill level to fight the" "\n" +
              "boss and possible catastrophy for Olfana." + "\n" + "\n" +
              "The final battle will be unlocked whenever your skill level passes" + "\n" +
              "the 20 point mark. Until then, you must prepare..." + "\n" + "\n" +
              f"Good luck {pc.name}!" + "\n")
        print("-" * 100)
        print()

        #STARTS STORY -------------------------------------------------------------------
        #fights battles continuously until ready for boss fight or dead

        player_dead = False

        while pc.skill < 20 and not player_dead and self.game.creatures != []:
            player_dead = self.fight_opponent()

        #STARTS BOSS FIGHT -------------------------------------------------------------------
        #starts boss fight if player hasn't died already

        if not player_dead:
            self.boss_fight()

    def fight_opponent(self):

        #FIGHT OPPONENT -------------------------------------------------------------------
        #selects and opponent, displays statistics and runs fight_battle

        self.game.choose_opponent()
        print("As you trek through the forest, you hear a noise from behind you and" + "\n" +
              "draw your sword *shwing*. A dark figure emerges from the trees..." + "\n" +
              f"... you have encountered {self.game.opponent.name}!\n")
        self.game.opponent.return_stats()
        print()

        player_dead = self.fight_battle()
        return player_dead

    def fight_battle(self):

        #FIGHT BATTLE --------------------------------------------------------------------
        #fights opponent until one of the two dies or the player flees

        flee = False
        round_num = 0

        while not flee and not self.game.opponent.is_dead and not self.game.player.is_dead:
            round_num += 1

            print("-" * 100)
            print(f"\nROUND {round_num}\n")
            choice = input(f"Would you like to fight a round against {self.game.opponent.name}? [y/n] ")
            print()

            if choice.lower() != "y":
                flee = True
                print("You flee, leaving your opponent behind. A cowardly but perhaps" + "\n" +
                      "strategic move." + "\n" + "\n" +
                      "'Till next time..', the foe mutters" + "\n"
                      "*You know there won't be a next time*")
            else:
                self.game.resolve_fight_round()
                self.game.return_round_result()

        if self.game.opponent.is_dead:
            self.opponent_dead()

        if self.game.player.is_dead:
            self.player_dead()
            return True
        else:
            return False

    def boss_fight(self):

        #BOSS FIGHT --------------------------------------------------------------------
        #fights boss goose as end point of the game

        self.game.boss_fight()
        self.game.choose_opponent()

        print("-" * 100)
        print()
        print("Traveller, after many a battle and drawn blood, you are reaching the" + "\n" +
              "conclusion of your quest. A singular looming foe waits in your path." + "\n" +
              "This is the inevitability that all of your valiant effort has led to" + "\n" +
              ", the one enemy.. you could never escape..." + "\n" + "\n" +
              f"... you have encountered {self.game.opponent.name}!\n" "\n" +
              "Unlike your past foes, this opponent has not been generated by the trivial" "\n" +
              "sum of dice but by the good hand of fate. With great stamina and skills" + "\n" +
              "you must mentally prepare for this tricky battle!" + "\n" + "\n" +
              f"This goose has stamina {self.game.opponent.stamina}, requiring multiples" + "\n" +
              "of the hits taken before for an ultimate defeat and only rivaled by the Wild" + "\n" +
              "Nendou." + "\n" + "\n" +
              f"It also has a skill level of {self.game.opponent.skill}, higher than" + "\n" +
              "any of those you have faced before..." + "\n" + "\n"
              "PREPARE TO FACE THE WILD GOOSE, TRUE MASTERMIND OF THE NECROSOFIA!!" + "\n" + "\n")

        round_num = 0

        while not self.game.player.is_dead and not self.game.opponent.is_dead:
            round_num += 1

            print("-" * 100)
            print(f"\nROUND {round_num}\n")
            choice = input(f"Would you like to fight a round against {self.game.opponent.name}? [y/n] ")

            if choice.lower() != "y":
                print("HAHA! Traveller, at this point, there is no point of return.." + "\n" +
                      "THIS, is a battle... to the DEATH!" + "\n" +
                      "*bum bum bummmm*" + "\n")

            self.game.resolve_fight_round()
            self.game.return_round_result()

            if self.game.round_result() == "win":
                print("The goose looks at you, and astounded look in its face.." + "\n" +
                      "'revenge...', you hear it mutter under its breath." + "\n")
            elif self.game.round_result() == "loss":
                print("*SQUAWK HONK*" + "\n")
            else:
                print("'interesting... interesting...', the goose looks at you" + "\n" +
                      "as it gauges your ability, cocking its neck to the side with" + "\n" +
                      "what can only be described as a look of pure hostility." + "\n")

        if self.game.opponent.is_dead:

            print("-" * 100)
            print()
            print("'How.. could a human... a PATHETIC... SMALL... human.. ever harm me?'" + "\n" + "\n"
                  "The goose stands in the fading sunlight, its eyes glossing over and its" + "\n"
                  "body starting to go limp. As it crumbles to ash before you very eyes" + "\n"
                  "you feel the pivot in the energy of the realm. The Necrosofia have been" + "\n"
                  "defeated and your mission is complete!" + "\n" + "\n")

        if self.game.player.is_dead:

            print("-" * 100)
            print()
            print("Failing... on the final hurdle... a truly pathetic end to and effortful" + "\n" +
                  "saga, all that for nought." + "\n" + "\n" +
                  "Thank you for aiding in the defence of Olfana... or at least your best" + "\n"
                  "effort to..." + "\n" + "\n"
                  "The goose looks you in the eyes, its own with an apathetic look as it flies" + "\n" +
                  "off into the distance..." + "\n" +
                  "'humans..' " + "\n" + "\n")

    def opponent_dead(self):

        #OPPONENT DEATH --------------------------------------------------------------------
        #increases player's stats after opponent defeated

        print("-" * 100)
        print(f"\n{str(self.game.opponent.name).upper()} HAS BEEN DEFEATED!! HUZZAH!" + "\n" + "\n" +
              "In return for your bravery, you have gained +2 skill and +4 stamina." + "\n" + "\n" +
              "Your new statistics are as follows..." + "\n")
        self.game.player.skill += 2
        self.game.player.stamina += 4
        self.game.player.return_stats()
        print()
        print("-" * 100)

    def player_dead(self):

        #PLAYER DEATH --------------------------------------------------------------------
        #player death sequence

        print("-" * 100)
        print(f"\n{self.game.player.name} has been defeated!" + "\n" + "\n" +
              "Traveller, despite your valiant effort, your quest comes to an end" + "\n" +
              "here, thank you for aiding in the defence of Olfana..." + "\n"
              "*insert roblox death sound*" + "\n")

    def game_fail(self):

        print("-" * 100)
        print()
        print("GAME OVER *bzzt*" + "\n" + "\n"
              "Finishing statistics are as follows..." + "\n")
        self.game.player.return_stats()
        print(f"Farwell {self.game.player.name}, we barely knew you..." + "\n")

    def game_success(self):

        print("-" * 100)
        print()
        print("GAME OVER *bzzt*" + "\n" + "\n"
              "Finishing statistics are as follows..." + "\n")
        self.game.player.return_stats()
        print(f"CONGRATULATIONS {(self.game.player.name).upper()}, YOU HAVE SAVED OLFANA!!" + "\n")

if __name__ == "__main__":
    GameCLI()