import pygame
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, color):
        super().__init__()

        self.image = pygame.Surface([4*radius, 4*radius])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.circle(self.image, color, (0, 0), radius, 20)

        self.rect = self.image.get_rect()
    
    def move(self, speedX, speedY):
        """
            updates the position of sprite on every frame
        """

        self.rect.x += speedX
        self.rect.y += speedY