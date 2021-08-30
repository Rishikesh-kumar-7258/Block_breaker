import pygame
from GameConstants.constants import *


#============= Text =====================#
def print_text(t, color, x,y, font_size, center=True):
    font = pygame.font.SysFont("Comic sans MS", font_size)
    text = font.render(t, True, color, BLACK)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    if center : SCREEN.blit(text, (textRect[0] - textRect[2] / 2, textRect[1] - textRect[3] / 2))
    else : SCREEN.blit(text, textRect)
#============= Text =====================#