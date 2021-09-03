import pygame

from States.Baseclass import Base
from Functions.textfunctions import *
from GameConstants.constants import *
from GameConstants.variables import *
from Classes.buttons import Button


startbtn = Button(x = WINDOW_WIDTH // 2 - 200, y = WINDOW_HEIGHT // 2 + 200, text="Next", color=GREEN, color2 = DARKGREEN)
settingsbtn = Button(x = WINDOW_WIDTH // 2 - 50, y = WINDOW_HEIGHT // 2 + 200, text="Settings", color=BLUE, color2 = DARKBLUE)
endbtn = Button(x = WINDOW_WIDTH // 2 + 100, y = WINDOW_HEIGHT // 2 + 200, text="Quit", color=RED, color2 = DARKRED)



class Over(Base):

    def __init__(self):
        super().__init__()

    def render(self):

        global startbtn, settingsbtn, endbtn

        print_text("Game Over!", RED, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 72)
        
        startbtn.render()
        settingsbtn.render()
        endbtn.render()

    def update(self, params):

        global startbtn, settingsbtn, endbtn, GAME_STATE_VARIABLES

        startbtn.update()
        settingsbtn.update()
        endbtn.update()

        if startbtn.clicked() : GAME_STATE_VARIABLES.change("play")
        if settingsbtn.clicked() : GAME_STATE_VARIABLES.change("settings")
        if endbtn.clicked() : 
            pygame.quit()
            quit()
        
        self.render()