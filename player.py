import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x,y,width , height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = "crimson"
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.radius = 50
        

    
    def draw(self,screen):
        pygame.draw.rect(screen, self.color,[self.x, self.y,self.height, self.width], 0, 2)
        self.s_size= pygame.display.get_window_size()
        self.s_height = self.s_size[1]
        self.s_width = self.s_size[0]



        
       
    def move_y(self, dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        
        self.y += 300 * dt
        self.color = "blue"

    def move_x(self, dt):
        #self.position += pygame.Vector2(self.x, self.y - dt)
        
        self.x += 300 * dt
        self.color = "crimson"
        
        
        
        
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.y >0:
                self.move_y(-dt)
        if keys[pygame.K_s]:
            if self.y < self.s_height - self.height:
                self.move_y(dt)
        if keys[pygame.K_a]:
            if self.x >0:
                self.move_x(-dt)
        if keys[pygame.K_d]:
            if self.x < self.s_width - self.width:
                self.move_x(dt)
    


