import pygame
from player import *
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
def main():
    clock =pygame.time.Clock()
    dt = 0
    player = Player(100, 100, 50,50)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        player .update(dt)
        screen.fill("grey")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    









if __name__ == "__main__":
    main()