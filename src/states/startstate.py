import pygame
from pygame.color import THECOLORS
from pygame.constants import K_DOWN, K_RETURN, K_UP, KEYDOWN, QUIT

from src.states.basestate import Base
from src.utilfuntions import Write

class Start(Base):

    """ This state is active when player has entered the game for the first time. """

    def __init__(self) -> None:
        super().__init__()

        self.options = ["Start", "Hight Scores"]
        self.active = 0
    
    def render(self) -> None:
        
        Write(self.screen, "Ball Breaker", self.screen_width // 2, self.screen_height // 2, 100, THECOLORS['darkgoldenrod'], True)
        
        for i in range(len(self.options)):
            color = THECOLORS['skyblue'] if i == self.active else THECOLORS['white']
            Write(self.screen, self.options[i].capitalize(), self.screen_width // 2, self.screen_height // 2 + i * 50 + 150, 50, color, True)

    def update(self, param):

        # event handlin in play state
        for event in param:

            # when key is pressed
            if event.type == KEYDOWN:

                # handling the navingation movement process
                if event.key == K_DOWN:
                    self.active = (self.active + 1) % len(self.options)
                if event.key == K_UP:
                    self.active -= 1
                    if self.active < 0 : self.active = len(self.options) - 1
                
                # when enter is pressed
                if event.key == K_RETURN:
                    state = None
                    if self.active == 0:
                        state = 'sliders'
                    elif self.active == 1:
                        state = 'highscore'
                    self.gstatemachine.change(state,    screen=self.screen,
                                                        gstatemachine=self.gstatemachine,
                                            )

        self.render()

    def enter(self, **params) -> None:
        
        self.__init__()

        self.screen = params['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = params['gstatemachine']