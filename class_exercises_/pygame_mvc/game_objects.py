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

    def move_character(self, character, pos):
        pass

    def find_objects_by_name(self, name):
        objects = []
        for thing in self.backgrounds:
            if thing.name == name:
                objects.append(thing)
        return objects

    def show_game_grid(self):
        pass


class GameObj:
    def __init__(self, controller, name, pos, solid):
        self.name = name
        self.pos = pos
        self.solid = solid

    def __repr__(self):
        return (f'name: {self.name}, pos: {self.pos}, solid: {self.solid}')

    def is_solid(self):
        return self.solid

class CharacterObj(GameObj):
    def __init__(self, controller, name):
        super().__init__(controller, name)

    def find_next_location(self, direction):
        if direction == 'W':
            return (self.pos[0], self.pos[1]+1)
        #TODO ts is not done

