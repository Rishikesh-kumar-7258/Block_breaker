import pygame
from stats import get_highScore
from statemachine import StateMachine

#============= SCORE WINDOW =================#
SCORE = 0
HIGH_SCORE = get_highScore()
LEVEL = 1
GAME_STATE_VARIABLES = StateMachine()
GAME_OVER = False
#============= SCORE WINDOW =================#
