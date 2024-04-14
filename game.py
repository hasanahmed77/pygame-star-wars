import pygame
from assets import *
from constants import *
from main import WIN

def draw_window(stormtrooper, boba_fett):
    WIN.fill(WHITE)
    WIN.blit(STORMTROOPER, (stormtrooper.x, stormtrooper.y))
    WIN.blit(BOBA_FETT, (boba_fett.x, boba_fett.y))
    pygame.display.update()

def moveCharacter(key_pressed, character, controls):
    if key_pressed[controls[0]]:
        character.x += VELOCITY
    elif key_pressed[controls[1]]:
        character.x -= VELOCITY
    elif key_pressed[controls[2]]:
        character.y -= VELOCITY
    elif key_pressed[controls[3]]:
        character.y += VELOCITY
