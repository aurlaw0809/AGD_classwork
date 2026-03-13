import pygame
from meteor_game import SpaceRocks

if __name__ == "__main__":
    pygame.init()
    space_rocks = SpaceRocks()
    space_rocks.main_loop()