import pygame
screen = pygame.display.set_mode((1280, 720))
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("white")
    









if __name__ == "__main__":
    main()