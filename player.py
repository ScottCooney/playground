import pygame
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x,y,width , height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = "crimson"
        self.can_jump = True
        self.jumping = False   
        self.jump_time = 0
    
        self.rotation = 0
        self.position = pygame.Vector2(x, y)

    
    def draw(self,screen):
        pygame.draw.rect(screen, self.color,[self.x, self.y,self.height, self.width], 0, 2)
        self.s_size= pygame.display.get_window_size()
        self.s_height = self.s_size[1]
        self.s_width = self.s_size[0]

    def rotate(self, dt):
        self.rotation += 200 * dt
        print(self.rotation)

        
       
    def move_y(self, dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        
            self.y += 500 * dt
            self.color = "blue"

    def jump(self,dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        if self.can_jump == True:
           # jump = (dt) * jump_height
          #  self.move_y(-jump)
          #  self.can_jump = False
          self.jump_time = 0.3
            
        
                           

    def move_x(self, dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        
        self.x += 500 * dt
        self.color = "crimson"
        
    def fall(self, dt):      
        self.y += 500 * dt
        
        
    
    def update(self, dt):
        self.jump_time -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.x >0:
                self.move_x(-dt)
        if keys[pygame.K_d]:
            if self.x < self.s_width - self.width:
                self.move_x(dt)
        if self.y <= screen_height - self.height and self.jump_time <=0:
            self.fall(dt)
        if  self.jump_time > 0:
            self.fall(-dt)
        if self.y >= screen_height - self.height:
            self.can_jump = True
        print(self.can_jump)
    


