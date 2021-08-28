import pygame
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)


        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, color, self.rect.center, min(self.rect.center))
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self, speedX, speedY):
        """
            updates the position of sprite on every frame
        """

        self.rect.x += speedX
        self.rect.y += speedY