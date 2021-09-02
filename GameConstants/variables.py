import pygame
from stats import get_highScore
from statemachine import StateMachine

#============= SCORE WINDOW =================#
HIGH_SCORE = get_highScore()
LEVEL = 0
GAME_STATE_VARIABLES = StateMachine()
GAME_OVER = False
#============= SCORE WINDOW =================#
