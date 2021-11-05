import pygame
from pygame.color import THECOLORS
from pygame.constants import K_LEFT, K_RETURN, K_RIGHT, KEYDOWN
from src.states.basestate import Base
from src.utilfuntions import get_score, Write
from src.spritesheet import SpriteSheet, buttons, sliders
from src.objects import BUTTON, SLIDER

class SliderChoosing(Base):

    """ This state is active after the start state or before the play state. """

    def __init__(self) -> None:
        super().__init__()

        self.sprite = SpriteSheet("images/spritesheet.png")
        self.highscores = get_score()
        self.slider_array = sliders(self.sprite)
        self.button_array = buttons(self.sprite)

    def render(self) -> None:

        Write(self.screen, "Press enter to choose", self.screen_width / 2, self.screen_height / 2 - 50, 72, THECOLORS['darkgoldenrod'], True)

        slider_image = self.slider_array[self.slider['number']]
        slider_rect = slider_image.get_rect()
        slider_rect.centerx = self.slider['x']
        slider_rect.y = self.slider['y']
        self.screen.blit(slider_image, slider_rect)

        left_image = self.button_array[self.left_button['number']]
        left_rect = left_image.get_rect()
        left_rect.centerx = self.left_button['x']
        left_rect.y = self.left_button['y']
        self.screen.blit(left_image, left_rect)

        right_image = self.button_array[self.right_button['number']]
        right_rect = right_image.get_rect()
        right_rect.centerx = self.right_button['x']
        right_rect.y = self.right_button['y']
        self.screen.blit(right_image, right_rect)

    def update(self, param) -> None:

        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.gstatemachine.change("play",   screen=self.screen, 
                                                        gstatemachine=self.gstatemachine,
                                                        slider_number=self.slider['number'])
                if event.key == K_RIGHT:
                    if self.slider['number'] < len(self.slider_array) - 1 : self.slider['number'] += 1
                if event.key == K_LEFT:
                    if self.slider['number'] > 0 : self.slider['number'] -= 1

        if self.slider['number'] == 0:
            self.left_button['number'] = 2
        else :
            self.left_button['number'] = 0

        if self.slider['number'] == len(self.slider_array) -1:
            self.right_button['number'] = 3
        else:
            self.right_button['number'] = 1
        
        self.render()
    
    def enter(self, **param) -> None:

        self.__init__()

        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        # making the slider 
        self.slider = SLIDER.copy()
        self.slider['x'] = self.screen_width / 2
        self.slider['y'] = self.screen_height / 2 + 20

        # making the left button
        self.left_button = BUTTON.copy()
        self.left_button['x'] = self.slider['x'] - 120
        self.left_button['y'] = self.slider['y']
        self.left_button['number'] = 2
        
        # making the right button
        self.right_button = BUTTON.copy()
        self.right_button['x'] = self.slider['x'] + 120
        self.right_button['y'] = self.slider['y']
        self.right_button['number'] = 1