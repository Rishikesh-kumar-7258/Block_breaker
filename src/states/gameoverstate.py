import pygame
from pygame.color import THECOLORS

from src.states.basestate import Base
from src.utilfuntions import Write

class GameOver(Base):

    """ This state is active when game is over. """

    def __init__(self) -> None:
        super().__init__()
        
        #options 
        self.options = ['Restart', 'Quit']
        
        # currently chosen option
        self.option = 1

    def render(self) -> None:
        
        Write(self.screen, "Game Over", self.screen_width / 2, self.screen_height/2, 72, THECOLORS['darkgoldenrod'], True)
        Write(self.screen, f"Score : {self.score}", self.screen_width / 2, self.screen_height/2 + 50, 32, THECOLORS['darkgoldenrod'], True)
        
        # Rendering the options
        for i in range(len(self.options)):
            color = THECOLORS['white']
            if i == self.option - 1:
                color = THECOLORS['skyblue']
            Write(self.screen, self.options[i], self.screen_width / 2, self.screen_height/2 + 150 + i*30, 32, color, True)
        
       
    def update(self, param):
    
        # event handling in game over state
        for event in param:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.option =  self.option -1 if self.option > 1 else  len(self.options)
                if event.key == pygame.K_DOWN:
                    self.option = (self.option + 1 )  if self.option < len(self.options) else 1
                if event.key == pygame.K_RETURN:
                    state = None
                    if self.option == 1:
                        self.gstatemachine.change("sliders", screen=self.screen, gstatemachine=self.gstatemachine)
                    elif self.option == 2:
                        pygame.quit()
                        quit()
                    
        self.render()
    
    def enter(self, **param):
        
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']
        self.score = param['score']