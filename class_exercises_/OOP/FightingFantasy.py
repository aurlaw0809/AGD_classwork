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

dragon = Character("Dragoneeeeeeeeeee", 10, 22)
jackie = Character("Jackie", 15, 25)
zippa = PC.generate_player_character("Zippa")