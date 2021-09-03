import pygame

from States.Baseclass import Base
from GameConstants.constants import *
from GameConstants.variables import *
from Classes.bubbles import Bubble
from Classes.ball import Ball
from Functions.textfunctions import *

#=================== SLIDER ===================#
slider = Bubble(60, 15, GREEN)
slider.x = WINDOW_WIDTH // 2 - 30
slider.y = WINDOW_HEIGHT - 20
slider.speed = 8
#=================== SLIDER ===================#

#=================== BALL ===================#
ball = Ball(RED)
ball.r = 8
ball.center = (WINDOW_WIDTH // 2, slider.y - ball.r - 6)
ball.speed = 5
#=================== BALL ===================#

#=================== BRICKS ===================#
bricks = show_bubbles(LEVEL)
#=================== BRICKS ===================#


class Play(Base):

    def __init__(self):
        super().__init__()

    def render(self):

        global slider

        slider.render()
        ball.render()

        for brick in bricks:
            brick.render()

    def update(self, params):

        global slider, LEVEL, bricks

        if ball.center[1] - ball.r >= WINDOW_HEIGHT : 
            GAME_STATE_VARIABLES.change("over")

        if ball.collides(slider) :
            ball.bounce(slider)

        for brick in bricks:
            if ball.collides(brick):
                ball.bounce(brick)
                bricks.remove(brick)

        if len(bricks) == 0 :
            LEVEL += 1
            GAME_STATE_VARIABLES.change("win")

        if slider.x >= WINDOW_WIDTH - 60 or slider.x <= 0 :
            slider.direction = 0

        if params == "left" :
            slider.direction = -1
        if params == "right" : slider.direction = 1
        if params == "released" :
            slider.direction = 0

        slider.update()
        ball.update()
        for brick in bricks :
            brick.update()
        self.render()

    def enter(self):

        global slider, ball, bricks

        ball.center = (WINDOW_WIDTH // 2, slider.y - ball.r - 6)
        slider.x = WINDOW_WIDTH // 2 - 30
        slider.y = WINDOW_HEIGHT - 20
        bricks = show_bubbles(LEVEL)