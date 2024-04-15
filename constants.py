import pygame
import os

# Initialize font
pygame.font.init()


# Game
HEALTH_FONT = pygame.font.Font(os.path.join('fonts', 'VT323-Regular.ttf'), 20)
WINNER_FONT = pygame.font.Font(os.path.join('fonts', 'VT323-Regular.ttf'), 80)
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 900, 500
CHARACTER_WIDTH, CHARACTER_HEIGHT = 40, 50
BULLET_WIDTH, BULLET_HEIGHT = 45, 7
BORDER_WIDTH = 1


# Character
STORMTROOPER_CONTROLS = (pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
BOBA_FETT_CONTROLS = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)
VELOCITY_CHARACTER = 5
HIT_STORMTROOPER = pygame.USEREVENT + 1
HIT_BOBA_FETT = pygame.USEREVENT + 2

# Bullet
VELOCITY_BULLET = 8
MAX_BULLETS = 3