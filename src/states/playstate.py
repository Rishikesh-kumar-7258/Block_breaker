import pygame
from pygame.color import THECOLORS
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, KEYUP
from src.levels import level
from src.objects import BALL, HEART, SLIDER

from src.states.basestate import Base
from src.spritesheet import SpriteSheet, blocks, balls, hearts, sliders
from src.utilfuntions import Write, collision

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

        self.block_score_array = [10, 10, 10, 20]

        # player properties
        self.score = 0
        self.lives_array = []
        self.lives = 3
        self.remaining_lives = self.lives

        # slider and ball properties
        self.slider_speed = 8
        self.current_slider_speed = 0
        self.ball_speed = 6
        self.current_ball_speed = (6, -6)


        self.paused = False
        
    def render(self) -> None:

        # rendering the header
        self.screen.blit(self.header, (0, 0))
        self.header.fill(THECOLORS["darkgreen"])
        for i in range(self.lives):
            image = self.heart_array[0] if self.lives_array[i]['alive'] else self.heart_array[1]
            image.set_colorkey(THECOLORS['white'])
            rect = image.get_rect()
            rect.centerx = self.lives_array[i]['x']
            rect.centery = self.lives_array[i]['y']
            self.header.blit(image, rect)
        Write(self.header, f"Score: {self.score}", 40, self.header_rect.centery, 24, THECOLORS['white'] , True)
        
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

        # rendering the ball
        ball_image = self.ball_array[self.ball['number']]
        ball_rect = ball_image.get_rect()
        ball_rect.centerx = self.ball['x']
        ball_rect.y = self.ball['y']
        self.screen.blit(ball_image, ball_rect)

        

    def update(self, param) -> None:

        # event handling in playstate
        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.current_slider_speed = self.slider_speed
                if event.key == K_LEFT:
                    self.current_slider_speed = -self.slider_speed
                
                if event.key == K_SPACE:
                    self.paused = not self.paused
            
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    self.current_slider_speed = 0
        
        self.render()

        # if the game is paused
        if self.paused:
            return

        # changing the position of slider
        if self.slider['x'] - self.slider['width'] /2 - 8 < 0:
            self.slider['x'] = self.slider['width'] / 2 + 8
        if self.slider['x'] + self.slider['width'] / 2 + 8 > self.screen_width:
            self.slider['x'] = self.screen_width - self.slider['width'] / 2 - 8
        self.slider['x'] += self.current_slider_speed

        # changing the position of ball
        if self.ball['x'] - self.ball['radius']  - 2 <= 0 or self.ball['x'] + self.ball['radius'] + 2 >= self.screen_width:
            a, b = self.current_ball_speed
            a *= -1
            self.current_ball_speed = (a, b)
        
        if self.ball['y'] + 2 < self.screen_height / 10:
            a, b = self.current_ball_speed
            b *= -1
            self.current_ball_speed = (a, b)

        if self.ball['y'] - self.ball['radius'] - 2 > self.screen_height:
            self.remaining_lives -= 1
            self.lives_array[self.remaining_lives]['alive'] = False
            self.ball['x'] = self.slider['x']
            self.ball['y'] = self.slider['y'] - self.ball['height'] - 2
            self.paused = True
        
        if self.remaining_lives == 0:
            self.gstatemachine.change('over', screen=self.screen, score=self.score, gstatemachine=self.gstatemachine)
        
        self.ball['x'] += self.current_ball_speed[0]
        self.ball['y'] += self.current_ball_speed[1]

        # handlind collision between ball and the slider
        if collision(self.ball, self.slider):
            a, b = self.current_ball_speed
            self.current_ball_speed = (a, -self.ball_speed)

        
        # handling the collision between ball and the blocks
        for block in self.all_blocks:
            if block['alive'] and collision(self.ball, block):
                block['number'] -= 1
                if block['number'] < 0:
                    block['alive'] = False
                a, b = self.current_ball_speed
                self.current_ball_speed = (a, self.ball_speed)
                self.score += self.block_score_array[block['number'] + 1]
    
    def enter(self, **params) -> None:

        self.__init__()

        self.screen = params['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = params['gstatemachine']
        self.slider_number = params['slider_number']

        # Making header for the game
        self.header = pygame.Surface((self.screen_width, self.screen_height/10))
        self.header.fill(THECOLORS['darkgreen'])
        self.header_rect = self.header.get_rect()

        for i in range(self.lives):
            heart = HEART.copy()
            heart['x'] = self.header_rect.right - 20 - i*20
            heart['y'] = self.header_rect.centery
            self.lives_array.append(heart)
        
        # getting the blocks
        self.all_blocks = level(self.screen, 0)

        # slider
        self.slider = SLIDER.copy()
        self.slider['x'] = self.screen_width // 2
        self.slider['y'] = self.screen_height - self.slider['height'] - 10
        self.slider['number'] = self.slider_number

        # Ball
        self.ball = BALL.copy()
        self.ball['x'] = self.screen_width // 2
        self.ball['y'] = self.slider['y'] - self.ball['height'] - 5
