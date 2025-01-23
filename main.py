import pygame
from player import *

screen = pygame.display.set_mode((1280, 720))
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock =pygame.time.Clock()
        dt = 0
        player = Player(50, 50)
        screen.fill("grey")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    









if __name__ == "__main__":
    main()