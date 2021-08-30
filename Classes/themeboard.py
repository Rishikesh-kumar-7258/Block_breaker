import pygame
from GameConstants.constants import *
from Functions.textfunctions import *


class Themeboard:

    count = 0

    def __init__(self, x, y, b_c, s_c, bl_c, t_c):

        self.count += 1

        board_size = 60
        s_width = 60
        s_height = 10
        bl_r = 5
        t_size = 15

        back = pygame.draw.rect(SCREEN, b_c, [x, y, board_size, board_size])
        print_text(str(self.count), WHITE, back.left-16, back.top, 16, False)
        s = pygame.draw.rect(SCREEN, s_c, [x, back.bottom - s_height, s_width, s_height])
        b = pygame.draw.circle(SCREEN, bl_c, (s.center[0], s.top - bl_r), bl_r)
        t = pygame.draw.rect(SCREEN, t_c, [back.center[0], back.top + 5, t_size, t_size])
        slider.change_color(s_c)

    
    def hover(self):
        mouse = pygame.mouse.get_pos()

        return (mouse[0] >= self.x and mouse[0] <= self.x + BUTTON_WIDTH) and (mouse[1] >= self.y and mouse[1] <= self.y + BUTTON_HEIGHT)
    def clicked(self):
        mouse = pygame.mouse.get_pressed()
        return (self.hover() and mouse[0])

    def change_theme(self):
        pass
