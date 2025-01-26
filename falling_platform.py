import pygame
from constants import *

class Falling_platform(pygame.sprite.Sprite):
    def __init__(self, x,y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.height = platform_height
        self.width = platform_width
        self.color = platform_color
    
    
    def draw(self,screen):
        pygame.draw.rect(screen, self.color,[self.x, self.y,self.width, self.height], 0, 2)
    

    def fall(self, dt):      
        self.y += 200 * dt


    def update(self, dt):
        if self.y > screen_height:
            self.kill()
            print("dead")
        self.fall(dt)
       