import pygame
pygame.init()

WIDTH = 15
HEIGHT = 15


class Boxes:

    """
        This is the blocks where the balls be shooted
    """
    
    def __init__(self, x=0, y=0, color=(0,0,0)):
        self.x = x
        self.y = y
        self.color = color
    
    def show(self,screen):
        """
            displaying the box
        """

        pygame.draw.rect(screen, self.color, (self.x, self.y, WIDTH, HEIGHT))


boxes = []

def Pattern(val, rows, cols, screen, color):
    if val == 1:
        for row in range(rows):
            temp = []
            for col in range(cols):
                to_add = Boxes((WIDTH+5)*col, (HEIGHT+5)*row, color)
                temp.append(to_add)
            boxes.append(temp)

    for box in boxes:
        for b in box:
            b.show(screen)