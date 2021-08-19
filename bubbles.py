import pygame
WHITE = (255, 255, 255)

class Bubble(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
    
    def move(self, speed, direction):
        """
            updates the position of sprite on every frame
        """

        self.rect.x += speed*direction