import pygame

# Constants
from constants import *

# Assets
from assets import STORMTROOPER, BOBA_FETT

# Game functions
from game import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('STAR WARS')

def main():
    stormtrooper = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    boba_fett = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        stormtrooper.x += 1
        draw_window(stormtrooper, boba_fett)
    
    pygame.quit()

if __name__ == "__main__":
    main()
