import pygame
from assets import *
from constants import *
from main import WIN

def draw_window(stormtrooper, boba_fett, bullets_stormtrooper, bullets_boba_fett, stormtrooper_health, boba_fett_health):
    WIN.blit(BACKGROUND, (0,0))

    pygame.draw.rect(WIN, BLACK, BORDER)

    stormtrooper_health_text = HEALTH_FONT.render(f"Health: {stormtrooper_health}", 1, WHITE)
    boba_fett_health_text = HEALTH_FONT.render(f"Health: {boba_fett_health}", 1, WHITE)

    WIN.blit(stormtrooper_health_text, (10, 10))
    WIN.blit(boba_fett_health_text, (WIDTH - boba_fett_health_text.get_width() - 10, 10))

    WIN.blit(STORMTROOPER, (stormtrooper.x, stormtrooper.y))
    WIN.blit(BOBA_FETT, (boba_fett.x, boba_fett.y))

    for bullet in bullets_stormtrooper:
        WIN.blit(STORMTROOPER_BULLET, (bullet.x, bullet.y))

    for bullet in bullets_boba_fett:
        WIN.blit(BOBA_FETT_BULLET, (bullet.x, bullet.y))

    pygame.display.update()

def draw_winner(text):
    winner_text = WINNER_FONT.render(text, 1, WHITE)

    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2 ))
    
    pygame.display.update()
    pygame.time.delay(2000)

def start_game():
    start_text = 'Press Enter to start.'

    draw_start_text = WINNER_FONT.render(start_text, 1, WHITE)

    WIN.blit(draw_start_text, (WIDTH // 2 - draw_start_text.get_width() // 2, HEIGHT // 2 - draw_start_text.get_height() // 2 ))

    pygame.display.update()

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_RETURN]:
        return True

def move_stormtrooper(key_pressed, character, controls):

    if key_pressed[controls[0]] and character.x + VELOCITY_CHARACTER + character.width< BORDER.x : # RIGHT
        character.x += VELOCITY_CHARACTER
    if key_pressed[controls[1]] and character.x - VELOCITY_CHARACTER  > 0: # LEFT
        character.x -= VELOCITY_CHARACTER
    if key_pressed[controls[2]] and character.y - VELOCITY_CHARACTER  > 0: # UP
        character.y -= VELOCITY_CHARACTER
    if key_pressed[controls[3]] and character.y + VELOCITY_CHARACTER + character.height < HEIGHT: # DOWN
        character.y += VELOCITY_CHARACTER

def move_boba_fett(key_pressed, character, controls):

    if key_pressed[controls[0]] and character.x + VELOCITY_CHARACTER + character.width < WIDTH : # RIGHT
        character.x += VELOCITY_CHARACTER
    if key_pressed[controls[1]] and character.x - VELOCITY_CHARACTER  > BORDER.x: # LEFT
        character.x -= VELOCITY_CHARACTER
    if key_pressed[controls[2]] and character.y - VELOCITY_CHARACTER  > 0: # UP
        character.y -= VELOCITY_CHARACTER
    if key_pressed[controls[3]] and character.y + VELOCITY_CHARACTER + character.height < HEIGHT: # DOWN
        character.y += VELOCITY_CHARACTER

def handle_bullet(bullets_stormtrooper, bullets_boba_fett, stormtrooper, boba_fett):
    for bullet in bullets_stormtrooper:
        bullet.x += VELOCITY_BULLET
        
        if boba_fett.colliderect(bullet):
            pygame.event.post(pygame.event.Event(HIT_BOBA_FETT))
            bullets_stormtrooper.remove(bullet)
        elif bullet.x > WIDTH:
            bullets_stormtrooper.remove(bullet)

    for bullet in bullets_boba_fett:
        bullet.x -= VELOCITY_BULLET

        if stormtrooper.colliderect(bullet):
            pygame.event.post(pygame.event.Event(HIT_STORMTROOPER))
            bullets_boba_fett.remove(bullet)
        elif bullet.x < 0:
            bullets_boba_fett.remove(bullet)
