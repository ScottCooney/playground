import pygame
from constants import *
from falling_platform import *
from gameobject import*


class Player(GameObject):
    def __init__(self, x,y):
        super().__init__(x,y)
        self.height = player_height
        self.width = player_width
        self.color = "crimson"
        self.can_jump = True
        self.jumping = False   
        self.jump_time = 0
        self.on_platform = False
        self.move_speed = player_move_speed     
        self.rotation = 0

        self.velocity = 0
        

    
    def draw(self,screen):
        pygame.draw.rect(screen, self.color,[self.x, self.y,self.height, self.width], 0, 2)
        self.s_size= pygame.display.get_window_size()
        self.s_height = self.s_size[1]
        self.s_width = self.s_size[0]

    def rotate(self, dt):
        self.rotation += 200 * dt
        print(self.rotation)


    
       
  #  def move_y(self, dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        
          #  self.y += self.move_speed * dt
            

    def jump(self,dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        if self.can_jump == True:
           # jump = (dt) * jump_height
          #  self.move_y(-jump)
          #  self.can_jump = False
          print("jump")
          self.jump_time = 0.5
          self.can_jump = False
        
            
        
                           

    def move_x(self, dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        
        self.x += self.move_speed  * dt
        self.color = "crimson"
    
    def fall(self, dt, speed):      
        self.y += speed  * dt
        

    def collide(self, Falling_platform):
        
        if self.x + self.height == Falling_platform.x:
            return True
        return False
    
    def update(self, dt):
        self.jump_time -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move_x(-dt)
            if self.x <=0:
                self.x = 0
        if keys[pygame.K_d]:
            self.move_x(dt)
            if self.x >= self.s_width - self.width:
                self.x = self.s_width - self.width
        if self.y <= screen_height - self.height and self.jump_time <=0:
            self.fall(dt, player_gravity)
        if self.jump_time>0:
            self.fall(-dt,player_jump_height)
        if self.y >= screen_height - self.height:
            self.y = screen_height - self.height
            self.can_jump = True
        
    


