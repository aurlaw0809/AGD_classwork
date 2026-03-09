from class_exercises_.pygame_mvc.game_objects import GameObj, CharacterObj

class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = (0, 0)
        self._start = (0, 0)
        self._end = (0, 0)

    def set_up(self, dimensions, start, end):
        self.dimensions = dimensions
        self._start = start
        self._end = end
        self.characters.append(CharacterObj(self,'Tom', (0, 5), True))

    def add_background_object(self, name, pos, solid):
        self.backgrounds.append(GameObj(self, name, pos, solid))

    def set_background_from_file(self, filename):
        with open(filename, 'r') as f:
            y = 0
            for thing in f.readlines():
                thing = thing.strip()
                x = 0
                for character in thing.split(','):
                    solid = False
                    if character == 'W':
                        solid = True
                    self.backgrounds.append(GameObj(self, character, (x, y), solid))
                    x += 1
                y += 1


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
        grid[self._start[1]][self._start[0]] = 'S'
        grid[self._end[1]][self._end[0]] = ' E'
        for thing in self.characters:
            grid[thing.pos[1]][thing.pos[0]] = thing.name[0]

        for row in range(rows):
            thisrow = []
            for col in range(cols):
                thisrow.append(grid[row][col])
            print(''.join(thisrow))
