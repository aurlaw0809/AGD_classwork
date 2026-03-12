class GameObj:
    def __init__(self, controller, name, pos, solid):
        self.name = name
        self.pos = pos
        self.solid = solid
        self.controller = controller

    def __repr__(self):
        return f'name: {self.name}, pos: {self.pos}, solid: {self.solid}'

    def is_solid(self):
        return self.solid

class CharacterObj(GameObj):
    def __init__(self, controller, name, pos, solid):
        super().__init__(controller, name, pos, solid)

    def find_next_location(self, direction):
        if direction == 'W':
            return self.pos[0], self.pos[1] - 1
        elif direction == 'A':
            return self.pos[0]-1, self.pos[1]
        elif direction == 'S':
            return self.pos[0], self.pos[1] + 1
        elif direction == 'D':
            return self.pos[0]+1, self.pos[1]
        return None

    def move(self, direction):
        self.pos = self.find_next_location(direction)

'''
game = Game()
game.set_up((12, 12), (0, 5), (11, 10))
game.set_background_from_file('mazemap.txt')
game.show_game_grid()
tom = CharacterObj(game, 'Tom', (0, 5), True))
'''