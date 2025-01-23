import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        self.position = pygame.Vector2(x, y)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.position.x,self.position.y , self.x ,self.y)

    def draw(self,screen):
        pygame.draw.rect(screen, "crimson", self.rect,5 )
    

