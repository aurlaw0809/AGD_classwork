import pygame
from pygame.image import load

def load_sprite(name, with_alpha=True):
    path = f"{name}.png"
    loaded_sprite = load(path)
    loaded_sprite = pygame.transform.scale(loaded_sprite, (800, 600))

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()