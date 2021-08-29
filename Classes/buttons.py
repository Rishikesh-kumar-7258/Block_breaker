import pygame

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

BLACK = (0,0,0)

class Button:
    def __init__(self, x, y, text, screen, color):

        self.x = x
        self.y = y
        self.color = color

        global BUTTON_WIDTH

        font = pygame.font.SysFont("Comic sans MS", 25)
        t = font.render(text, True, BLACK, color)
        textRect = t.get_rect()
        textRect.center = (x + BUTTON_WIDTH/2, y+BUTTON_HEIGHT/2)
        if (textRect[2] > BUTTON_WIDTH) : BUTTON_WIDTH = textRect[2] + 20
        button = pygame.draw.rect(screen, color, [x, y, BUTTON_WIDTH, BUTTON_HEIGHT])
        screen.blit(t, textRect)

    def hover(self):
        mouse = pygame.mouse.get_pos()

        return (mouse[0] >= self.x and mouse[0] <= self.x + BUTTON_WIDTH) and (mouse[1] >= self.y and mouse[1] <= self.y + BUTTON_HEIGHT)