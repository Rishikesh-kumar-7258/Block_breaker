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
ball.center = (WINDOW_WIDTH // 2, slider.y- ball.r - 2)
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

        for brick in bricks: brick.render()
    
    def update(self, params):

        global slider

        if ball.collides(slider) : ball.bounce(slider)

        for brick in bricks:
            if ball.collides(brick): 
                ball.bounce(brick)
                brick.erase()

        if slider.x >= WINDOW_WIDTH - 60 or slider.x <= 0 : slider.direction = 0

        if params == "left" : slider.direction = -1
        if params == "right" : slider.direction = 1
        if params == "released" : slider.direction = 0


        slider.update()
        ball.update()
        for brick in bricks : brick.update()
        self.render()