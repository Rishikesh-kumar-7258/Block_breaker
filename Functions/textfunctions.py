import pygame
from GameConstants.constants import *
from levels import *


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

def show_bubbles(level):
    if (level == 0) : test(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))
    elif (level == 1) : level1(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))
    elif (level == 2) : level2(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))
    elif (level == 3) : level3(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))