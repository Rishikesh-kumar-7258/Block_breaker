import pygame
from pygame.color import THECOLORS
from pygame.constants import K_RETURN, KEYDOWN

from src.states.basestate import Base
from src.utilfuntions import Write, get_score

class Highscore(Base):

    """ This state is active after the player clicks highscore button in startscreen. """

    def __init__(self) -> None:
        super().__init__()

        self.scores = get_score()

    def render(self) -> None:

        Write(self.screen, "Highscores", self.screen_width/2, 40, 72, THECOLORS['darkgoldenrod'], True)
        
        i = 0
        for player in self.scores:
            name, score = player
            Write(self.screen, f"{i+1}.    {name}    {score}", self.screen_width/2, i*40+100, 48, THECOLORS['white'], True)
            i += 1
            if (i == 10):
                break
        
        Write(self.screen, "Back", self.screen_width/2, self.screen_height-40, 48, THECOLORS['skyblue'], True)

    def update(self, param) -> None:

        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.gstatemachine.change('start', screen=self.screen, gstatemachine=self.gstatemachine)
        
        self.render()
    
    def enter(self, **params) -> None:
        
        self.screen = params['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = params['gstatemachine']