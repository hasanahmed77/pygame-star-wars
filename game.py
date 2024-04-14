from assets import *
from constants import *
from main import WIN

def draw_window(stormtrooper, boba_fett):
    WIN.fill(WHITE)
    WIN.blit(STORMTROOPER, (stormtrooper.x, stormtrooper.y))
    WIN.blit(BOBA_FETT, (boba_fett.x, boba_fett.y))
    pygame.display.update()