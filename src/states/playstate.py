import pygame
from pygame.color import THECOLORS
from src.objects import HEART

from src.states.basestate import Base
from src.spritesheet import SpriteSheet, blocks, balls, hearts, sliders
from src.utilfuntions import Write

class Play(Base):

    """ This state is active when player is currently playing the game. """

    def __init__(self) -> None:
        super().__init__()

        # spritesheet
        self.sprite = SpriteSheet("images/spritesheet.png")

        # Differnt sprites
        self.block_array = blocks(self.sprite)
        self.ball_array = balls(self.sprite)
        self.slider_array = sliders(self.sprite)
        self.heart_array = hearts(self.sprite)

        # player properties
        self.score = 0
        self.lives_array = []
        self.lives = 3

        
    def render(self) -> None:

        # rendering the header
        self.screen.blit(self.header, (0, 0))
        for i in range(self.lives):
            image = self.heart_array[0] if self.lives_array[0]['alive'] else self.heart_array[1]
            image.set_colorkey(THECOLORS['white'])
            rect = image.get_rect()
            rect.centerx = self.lives_array[i]['x']
            rect.centery = self.lives_array[i]['y']
            self.header.blit(image, rect)

        

    def update(self, param) -> None:

        self.render()
    
    def enter(self, **params) -> None:

        self.__init__()

        self.screen = params['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = params['gstatemachine']

        # Making header for the game
        self.header = pygame.Surface((self.screen_width, self.screen_height/10))
        self.header.fill(THECOLORS['darkgreen'])
        self.header_rect = self.header.get_rect()
        Write(self.header, f"Score: {self.score}", 40, self.header_rect.centery, 24, THECOLORS['white'] , True)

        for i in range(self.lives):
            heart = HEART.copy()
            heart['x'] = self.header_rect.right - 20 - i*20
            heart['y'] = self.header_rect.centery
            self.lives_array.append(heart)
