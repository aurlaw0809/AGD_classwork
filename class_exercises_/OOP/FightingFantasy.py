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

dragon = Character("Dragoneeeeeeeeeee", 10, 22)