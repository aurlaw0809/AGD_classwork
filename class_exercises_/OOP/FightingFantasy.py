import random

def dice_sum(num_dice: int = 1, num_sides: int = 6):
    """howdy
    there"""
    total = sum(random.randint(1, num_sides) for number in range(num_dice))
    return total

class Character:
    def __init__(self, name: str, skill: int, stamina: int):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def return_stats(self):
        print(f"{self.name} stats!" + "\n" +
              f"Skill     {self.skill}" + "\n" +
              f"Stamina   {self.stamina}")

    def __str__(self):
        return f"{self.name}"

    def find_score(self):
        self.roll = dice_sum(2)
        self.score = self.roll + self.skill

    def take_hit(self, damage: int=2):
        self.stamina -= damage

    def fight_round(self, other):
        self.find_score()
        other.find_score()

        if self.score > other.score:
            other.take_hit()
            return 'win!'
        elif self.score < other.score:
            self.take_hit()
            return 'loss..'
        else:
            self.take_hit(1)
            other.take_hit(1)
            return 'draw..?'

    def return_character_status(self):
        return f'{self.name} has {self.stamina} stamina(s) left and skill {self.skill}'

    def return_rolls_status(self):
        return f'{self.name} rolled {self.roll} for a total score of {self.score}'

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self, dead: bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina, 1)

class NPC(Character):
    pass

class PC(Character):
    def __init__(self, name: str, skill: int, stamina: int, luck: int):
        super().__init__(name, skill, stamina)
        self.luck = luck

    @classmethod
    def generate_player_character(cls, name):
        return cls(name, skill = dice_sum(2), stamina = dice_sum(2), luck = dice_sum(2))

    def __repr__(self):
        return f"PlayerCharacter('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"

    def return_stats(self):
        print(f"{self.name} stats!" + "\n" +
              f"Skill     {self.skill}" + "\n" +
              f"Stamina   {self.stamina}" + "\n" +
              f"Luck      {self.luck}")

    def test_luck(self):
        score = dice_sum(2)
        self.roll = score

        if score <= self.luck:
            self.luck -= 1
            return True
        else:
            self.luck -= 1
            return False

zippa = PC.generate_player_character("Zippa :|")

class Game:
    @classmethod
    def load_creatures(cls):
        creatures = [Character("Snek", 3, 5),
                     Character("Box Fish", 5, 3),
                     Character("Leonardo DaVinci", 8, 4),
                     Character("Dragon", 8, 12),
                     Character("Jackie", 10, 7),
                     Character("Coin man", 12, 4),
                     Character("Sir Tom", 6, 4),
                     Character("Batman", 10, 9),
                     Character("Batsman", 11, 10),
                     Character("Meghahn", 5, 5)
                     ]
        return creatures

    def load_boss(cls):
        boss = Character("Wild goose", 12, 12)
        return boss

    def __init__(self):
        self.opponent = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures()

    def choose_opponent(self):
        self.opponent = random.choice(self.creatures)
        self.creatures.remove(self.opponent)

    def set_player(self, player_character):
        self.player = player_character

    def resolve_fight_round(self):
        self.round_result = self.player.fight_round(self.opponent)

    def return_character_status(self):
        return f'{self.player.name} has {self.player.stamina} stamina(s) left and skill {self.player.skill}'

    def return_round_result(self):
        msg = f"{self.player.return_rolls_status()}" + "\n" + f"{self.opponent.return_rolls_status()}" + "\n"

        if self.round_result == 'win!':
            msg += "Player wins!\n"

        elif self.round_result == 'loss..':
            msg += "Player loses :(\n"
        else:
            msg += "This round was a draw...\n"

        print(msg)

        if self.opponent.is_dead:
            self.opponent_dead()

        if self.player.is_dead:
            self.player_dead()

    def opponent_dead(self):
        print(f"\n{self.opponent.name} has been defeated!! HUZZAH!" + "\n" + "\n" +
                "In return for your bravery, you have gained +1 skill and +4 stamina." + "\n" +
                "Your new statistics are as follows..." + "\n")
        self.player.skill += 1
        self.player.stamina += 4
        self.player.return_stats()

    def player_dead(self):
        print(f"\n{self.player.name} has been defeated!" + "\n" + "\n" +
              "Traveller, despite your valiant effort, your quest comes to an end" + "\n" +
              "here, thank you for aiding in the defence of Olfana...")

    def boss_fight(self):
        self.creatures = self.load_boss()
        #add on to this?


'''
game = Game()
goose = PC.generate_player_character("Goose!!")
game.set_player(goose)
game.choose_opponent()
game.resolve_fight_round()
game.return_round_result()
'''