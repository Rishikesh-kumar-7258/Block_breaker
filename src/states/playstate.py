import pygame
from pygame.color import THECOLORS
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP
from src.levels import level
from src.objects import BALL, HEART, SLIDER

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

        # slider and ball properties
        self.slider_speed = 6
        self.current_slider_speed = 0
        self.ball_speed = (6, 6)
        self.current_ball_speed = (6, 6)

        
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
        
        # rendering the blocks on the screen
        for block in self.all_blocks:
            if block['alive']:
                image = self.block_array[block['number']]
                rect = image.get_rect()
                rect.x = block['x']
                rect.y = block['y']
                self.screen.blit(image, rect)
        
        # rendering the slider
        slider_image = self.slider_array[self.slider['number']]
        slider_rect = slider_image.get_rect()
        slider_rect.centerx = self.slider['x']
        slider_rect.y = self.slider['y']
        self.screen.blit(slider_image, slider_rect)

        

    def update(self, param) -> None:

        # event handling in playstate
        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.current_slider_speed = self.slider_speed
                if event.key == K_LEFT:
                    self.current_slider_speed = -self.slider_speed
            
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    self.current_slider_speed = 0
        
        # changing the position of slider
        if self.slider['x'] - self.slider['width'] /2 - 8 < 0:
            self.slider['x'] = self.slider['width'] / 2 + 8
        if self.slider['x'] + self.slider['width'] / 2 + 8 > self.screen_width:
            self.slider['x'] = self.screen_width - self.slider['width'] / 2 - 8
        self.slider['x'] += self.current_slider_speed

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
        
        # getting the blocks
        self.all_blocks = level(self.screen, 0)

        # Ball and slider
        self.slider = SLIDER.copy()
        self.slider['x'] = self.screen_width // 2
        self.slider['y'] = self.screen_height - self.slider['height'] - 10
        self.ball = BALL.copy()
        self.ball['x'] = self.screen_width // 2
        self.slider['y'] = self.slider['y'] + 5
