import pygame
from class_exercises_.pygame_mvc.game_controller import Game

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SQUARE_SIZE = 50

BACKGROUND_COLORS = {'W': (120, 176, 69),
                     'S': (204, 111, 61),
                     'E': (224, 176, 92),
                     'F': (219, 227, 127)
                     }
PLAYER_COLOR = (173, 39, 36)

class GameGUI:
    key_moves = {K_UP: 'W',
                 K_DOWN: 'S',
                 K_RIGHT: 'A',
                 K_LEFT: 'D',
                 }

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame MVC')

        # Set clock so that FPS can be limited
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.game.set_up((12, 12), (0, 5), (11, 10))
        self.game.set_background_from_file('mazemap.txt')
        self.player = self.game.characters[0]
        self.move_direction: str | None = None

        self.screen = pygame.display.set_mode([self.game.dimensions[1] * SQUARE_SIZE,
                                               self.game.dimensions[0] * SQUARE_SIZE])
        self.running = True
        self.exit_found = False

        self.player_image = pygame.image.load('tom.png').convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (SQUARE_SIZE, SQUARE_SIZE))
        self.player_rect = self.player_image.get_rect()

    @staticmethod
    def _convert_position(pos, center: bool = False) -> tuple[int, int]:
        """ Convert a grid position in the game to an (x, y) coordinate
                if centre is false the position returned is top-left and if center is true
                the position returned is the centre """
        x = pos[0] * SQUARE_SIZE
        y = pos[1] * SQUARE_SIZE
        return x, y

    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60) # cap to 60 FPS
        pygame.quit()

    def _handle_input(self):
        """ Checks key presses and adjusts GameGUI attributes depending on the presses """

        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            if event.type == KEYDOWN and self.running:
                if event.key == K_LEFT:
                    self.move_direction = 'A'
                elif event.key == K_RIGHT:
                    self.move_direction = 'D'
                elif event.key == K_UP:
                    self.move_direction = 'W'
                elif event.key == K_DOWN:
                    self.move_direction = 'S'
                else:
                    self.move_direction = None

            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None
            ...

    def _process_game_logic(self):
        """ Implements character moves and checks if player has reached the exit """
        if self.running and self.move_direction is not None:
            self.game.move_character(self.player, self.move_direction)
            self.move_direction = None

        if self.player.pos == self.game.end:
            self.running = False
            self.exit_found = True

        ...

    def _draw(self):
        """draw background first then characters"""
        self._draw_background()
        self._draw_characters()
        ...
        pygame.display.flip()

    def _draw_background(self):
        """Loop through all the game backgrounds and draw a rectangle of the appropriate colour"""
        self.screen.fill(BACKGROUND_COLORS['F'])
        for thing in self.game.backgrounds:
            position = self._convert_position(thing.pos)
            colour = BACKGROUND_COLORS[thing.name.strip()]
            pygame.draw.rect(self.screen, colour, (position[0], position[1], SQUARE_SIZE, SQUARE_SIZE), 0)
            #something
        ...

    def _draw_characters(self):
        """Loop through the characters and draw a circle for each character"""
        for character in self.game.characters:
            position = self._convert_position(character.pos, True)
            self.player_rect.center = (position[0]+SQUARE_SIZE/2, position[1]+SQUARE_SIZE/2)
            self.screen.blit(self.player_image, self.player_rect)
        ...

if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()