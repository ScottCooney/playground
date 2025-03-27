import pygame
import random
from constants import *
from falling_platform import *


class Platform_Spawner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.min_x = 0
        self.max_x = screen_width - platform_width
        self.spawn_time = 0


    def spawn_plat(self):
        plat_x = random.randint(self.min_x,self.max_x)
        new_plat = Falling_platform(plat_x,0)
        self.spawn_time = 1

    def update(self, dt):
        self.spawn_time -= dt   

        if self.spawn_time <= 0:
            self.spawn_plat()