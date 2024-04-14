import pygame
import os
from constants import *
# Assets
STORMTROOPER_IMG = pygame.image.load(
    os.path.join('Assets', 'stormtrooper.png'))

BOBA_FETT_IMG = pygame.image.load(
    os.path.join('Assets', 'boba-fett.png')
)

# Scaling characters
STORMTROOPER = pygame.transform.scale(STORMTROOPER_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
BOBA_FETT = pygame.transform.scale(BOBA_FETT_IMG, (CHARACTER_WIDTH, CHARACTER_HEIGHT))