class Game:
    def __init__(self, controller):
        self.characters = []
        self.backgrounds = []
        self.dimensions = (0, 0)
        self._start = (0, 0)
        self._end = (0, 0)

    def set_up(self, dimensions, start, end):
        self.dimensions = dimensions
        self._start = start
        self._end = end

    def add_background_object(self, name, pos, solid):
        self.backgrounds.append(GameObj(self, name, pos, solid))

    def set_background_from_file(self, filename):
        with open(filename, 'r') as f:
            objects = f.readlines()
            for thing in objects:
                thing = thing.strip()
                name, pos, solid = thing.split(',')
                self.add_background_object(name, pos, solid)

    def check_collisions(self, pos):
        for thing in self.backgrounds:
            if thing.pos == pos:
                if thing.solid:
                    return True
                else:
                    return False
        return None
    #true = there IS a collision

    def get_cell_contents(self, pos):
        contents = []
        for thing in self.backgrounds:
            if thing.pos == pos:
                contents.append(thing)
        return contents

    def move_character(self, character, direction):
        mv = False
        new_pos = character.find_next_location(direction)
        if not self.check_collisions(new_pos):
            character.move(direction)
            mv = True
        return mv

    def find_objects_by_name(self, name):
        objects = []
        for thing in self.backgrounds:
            if thing.name == name:
                objects.append(thing)
        return objects

    def show_game_grid(self):
        rows = self.dimensions[1]
        cols = self.dimensions[0]

        grid = [['' for y in range(cols)] for x in range(rows)]

        for thing in self.backgrounds:
            grid[thing.pos[1]][thing.pos[0]] = thing.name
        for thing in self.characters:
            grid[thing.pos[1]][thing.pos[0]] = thing.name
        grid[self._start[1]][self._start[0]] = 'S'
        grid[self._end[1]][self._end[0]] = 'E'

        for row in range(rows):
            for col in range(cols):
                print(grid[row][col])

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
    def __init__(self, controller, name):
        super().__init__(controller, name)

    def find_next_location(self, direction):
        if direction == 'W':
            return self.pos[0], self.pos[1] + 1
        elif direction == 'A':
            return self.pos[0]-1, self.pos[1]
        elif direction == 'S':
            return self.pos[0]+1, self.pos[1]
        elif direction == 'D':
            return self.pos[0], self.pos[1]-1
        return None

    def move(self, direction):
        self.pos = self.find_next_location(direction)