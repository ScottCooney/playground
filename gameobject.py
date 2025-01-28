import pygame
from constants import *


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x,y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y

    def update(self, dt):
        pass