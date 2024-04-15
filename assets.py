import pygame
import os
from constants import *

# Assets
STORMTROOPER_IMG = pygame.image.load(
    os.path.join('Assets', 'stormtrooper-2.png'))

BOBA_FETT_IMG = pygame.image.load(
    os.path.join('Assets', 'boba-fett-2.png')
)

STORMTROOPER_BULLET_IMG = pygame.image.load(
    os.path.join('Assets', 'stormtrooper-blaster-2.png')
)

BOBA_FETT_BULLET_IMG = pygame.image.load(
    os.path.join('Assets', 'boba-fett-blaster-2.png')
)

BACKGROUND_IMG = pygame.image.load(
    os.path.join('Assets', 'background.jpg')
)

# Sound Effects
BULLET_HIT_SOUND = pygame.mixer.Sound(
    os.path.join('Assets', 'Gun+Silencer.mp3')
)

BULLET_FIRE_STORMTROOPER = pygame.mixer.Sound(
    os.path.join('Assets', 'stormtrooper-blaster.mp3')
) 

BULLET_FIRE_BOBA_FETT = pygame.mixer.Sound(
    os.path.join('Assets', 'boba-fett-blaster.mp3')
) 

BACKGROUND_MUSIC = pygame.mixer.Sound(
    os.path.join('Assets', 'background-music.mp3')
)


BORDER = pygame.Rect(WIDTH // 2 - BORDER_WIDTH, 0, BORDER_WIDTH, HEIGHT)

# Scaling characters 
STORMTROOPER = pygame.transform.scale(STORMTROOPER_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
BOBA_FETT = pygame.transform.scale(BOBA_FETT_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

# Scaling bullets
STORMTROOPER_BULLET = pygame.transform.scale(STORMTROOPER_BULLET_IMG, (BULLET_WIDTH, BULLET_HEIGHT))
BOBA_FETT_BULLET = pygame.transform.scale(BOBA_FETT_BULLET_IMG, (BULLET_WIDTH, BULLET_HEIGHT))

# Scaling background
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))