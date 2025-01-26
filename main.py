import pygame
from player import *
from falling_platform import *
from constants import *




screen = pygame.display.set_mode((screen_width,screen_height))
def main():

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Falling_platform.containers = (updatable, drawable)
    clock =pygame.time.Clock()
    dt = 0
    player = Player(100, 100, 50,50)
    platform = Falling_platform(300,300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.jump(dt)
                player.can_jump == False
                    
       
        for obj in updatable:
            obj.update(dt)


        screen.fill("grey")

        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
    








if __name__ == "__main__":
    main()