import pygame
pygame.init()

WIDTH = 30
HEIGHT = 10
SPEED = 1

class Support:
    """
        supporting block class
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = SPEED

    
    def render(self, screen, color):
        """
            rendering the supporting block
        """
        pygame.draw.rect(screen, color, (self.x, self.y, WIDTH, HEIGHT))
    
    def changePos(self, val):
        """
            changing the position of the block
        """
        
        self.x += SPEED*val
