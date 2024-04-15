import pygame, sys
pygame.mixer.init()

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

    bullets_stormtrooper = []
    bullets_boba_fett = []

    stormtrooper_health = 10
    boba_fett_health = 10

    game_over_text = ""

    clock = pygame.time.Clock()

    run_start_game = True
    while run_start_game:
        WIN.blit(BACKGROUND, (0,0))
        start_text = 'Press Enter to start.'

        draw_start_text = WINNER_FONT.render(start_text, 1, WHITE)

        WIN.blit(draw_start_text, (WIDTH // 2 - draw_start_text.get_width() // 2, HEIGHT // 2 - draw_start_text.get_height() // 2 ))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                run_start_game = False
        pygame.display.update()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Stormtrooper
                if event.key == pygame.K_SPACE and len(bullets_stormtrooper) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        stormtrooper.x + stormtrooper.width // 2, 
                        stormtrooper.y + stormtrooper.height // 100, 
                        BULLET_WIDTH, 
                        BULLET_HEIGHT)
                    bullets_stormtrooper.append(bullet)
                    BULLET_FIRE_STORMTROOPER.play()

                # Boba Fett
                if event.key == pygame.K_RETURN and len(bullets_boba_fett) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        boba_fett.x, 
                        boba_fett.y + boba_fett.height // 100, 
                        BULLET_WIDTH, 
                        BULLET_HEIGHT)
                    bullets_boba_fett.append(bullet)
                    BULLET_FIRE_BOBA_FETT.play()
            
            if event.type == HIT_STORMTROOPER:
                stormtrooper_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == HIT_BOBA_FETT:
                boba_fett_health -= 1
                BULLET_HIT_SOUND.play()
            
        if stormtrooper_health <= 0:
            game_over_text = 'Boba Fett wins!'
        elif boba_fett_health <= 0:
            game_over_text = 'Stormtrooper wins!'
        elif boba_fett_health <= 0 and stormtrooper_health <= 0:
            game_over_text = 'Worthy Opponent. DRAW!'
        
        if game_over_text != "":
            draw_winner(game_over_text)
            break
            
        key_pressed = pygame.key.get_pressed()

        # Move Stormtrooper
        move_stormtrooper(key_pressed, stormtrooper, STORMTROOPER_CONTROLS)

        # Move Boba Fett
        move_boba_fett(key_pressed, boba_fett, BOBA_FETT_CONTROLS)

        # Handle bullets
        handle_bullet(
            bullets_stormtrooper, 
            bullets_boba_fett, 
            stormtrooper, 
            boba_fett
            )

        # UI
        draw_window(
            stormtrooper, 
            boba_fett, 
            bullets_stormtrooper, 
            bullets_boba_fett, 
            stormtrooper_health, 
            boba_fett_health
            )
        
    main()

if __name__ == "__main__":
    main()
