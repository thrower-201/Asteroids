import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        pygame.display.flip() 
    pygame.init()
    
if __name__ == "__main__":
    main()
