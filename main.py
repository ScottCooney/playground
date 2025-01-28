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
    player = Player(100, 100)
    platform = Falling_platform(300,700)
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.jump(dt)
                   
                    
                    
       
        for obj in updatable:
            obj.update(dt)


        screen.fill("grey")

        
        if player.collide(platform) == True:
            player.on_platform = True
            print("ont plat")
        
        for obj in drawable:
            obj.draw(screen)
        
        coordinates_text = f"X: {player.x}, Y: {player.y}"
        text_surface = font.render(coordinates_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))


        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
    








if __name__ == "__main__":
    main()