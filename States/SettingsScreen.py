import pygame

from States.Baseclass import Base
from Functions.textfunctions import *
from Classes.themeboard import Themeboard
from Classes.buttons import Button
from GameConstants.variables import *
from GameConstants.constants import *

SLIDER_COLOR = GREEN
BALL_COLOR = RED
TILE_COLOR = LIGHTBLUE
BACKGROUND_COLOR = BLACK

# width = 60, height = 60
board1 = Themeboard(x=20, y=60, b_c=GRAY, s_c=GREEN, bl_c=RED, t_c=LIGHTBLUE, count=1)
board2 = Themeboard(x=100, y=60, b_c=GRAY, s_c=BLUE, bl_c=GREEN, t_c=CHOCOLATY, count=2)

backbtn = Button(x = WINDOW_WIDTH // 2 - 100, y = WINDOW_HEIGHT // 2 + 200, text="back", color=GREEN, color2 = DARKGREEN)



class Settings(Base):

    def __init__(self):
        super().__init__()

        self.boards = []
        self.boards.append(board1)
        self.boards.append(board2)

    def render(self):

        print_text("Click on the board to change theme", BLUE, WINDOW_WIDTH // 2, 30, 36)

        for board in self.boards:
            board.render()
        
        backbtn.render()

    def update(self, params):

        global SLIDER_COLOR, BALL_COLOR, BACKGROUND_COLOR, TILE_COLOR, GAME_STATE_VARIABLES
        
        for board in self.boards:
            if board.clicked():
                SLIDER_COLOR = board.slider_color
                BALL_COLOR = board.ball_color
                BACKGROUND_COLOR = board.background_color
                TILE_COLOR = board.tile_color
            
        backbtn.update()
        if backbtn.clicked() : GAME_STATE_VARIABLES.change("TitleScreen")

        self.render()