import pygame
from constants import *

def main():
    # Initialize dependency
    pygame.init()
    # Set up GUI window size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game inifinite loop
    while True:
        # Turn the screen black
        screen.fill("black")
        # Refresh the screen
        pygame.display.flip()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
