import pygame

from src.spritesheet import SpriteSheet, balls, blocks, sliders
from src.statemachine import Statemachine
from src.states.gameoverstate import GameOver
from src.states.highscoreState import Highscore
from src.states.levelpassedstate import LevelPassed
from src.states.playstate import Play
from src.states.sliderchoosingstate import SliderChoosing
from src.states.startstate import Start

pygame.init()

# parameters for the screen
screen_width = 800
screen_height = 600

# Setting up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")
pygame.display.set_icon(pygame.image.load("images/logo.png"))

# differenst states
gameStates = {
    "start" : Start(),
    "sliders" : SliderChoosing(),
    "highscore" : Highscore(),
    "play" : Play(),
    "levelclear" : LevelPassed(),
    "over" : GameOver()
}

# statemachine
gstatemachine = Statemachine(gameStates)
gstatemachine.change("start",   screen=screen,
                                gstatemachine=gstatemachine
                    )
gstatemachine.render()

# spritesheet
sprite = SpriteSheet("images/spritesheet.png")
block_array = blocks(sprite)
ball_array = balls(sprite)
slider_array = sliders(sprite)

# setting up the clock
clock = pygame.time.Clock()

# setting up the game loop
running = True
while running:
    # event handling
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # drawing and updating the screen
    screen.fill((0, 0, 0))
    gstatemachine.update(events)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()