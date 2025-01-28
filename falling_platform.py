import pygame
from constants import *
from gameobject import *

class Falling_platform(GameObject):
    def __init__(self, x,y):
        super().__init__(x,y)
        self.height = platform_height
        self.width = platform_width
        self.color = platform_color
        self.position = pygame.Vector2(x, y)
        self.will_fall = False
    
    
    def draw(self,screen):
        pygame.draw.rect(screen, self.color,[self.x, self.y,self.width, self.height], 0, 2)
    

    def fall(self, dt):      
        self.y += 50 * dt


    def update(self, dt):
        if self.y > screen_height: 
            self.kill()
            print("dead")
        if self.will_fall == True:    
            self.fall(dt)
       