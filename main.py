import pygame

from GameConstants.constants import *
from statemachine import StateMachine
from States.TitleScreen import Title
from States.PlayScreen import Play

pygame.init()

STATES = {
    "TitleScreen" : Title(),
    "play" : Play(),
    "settings" : Settings()
}

GAME_STATE_VARIABLES = StateMachine(STATES)

GAME_STATE_VARIABLES.change("TitleScreen")


while not GAME_OVER:

    pressed_key = None
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            GAME_OVER = True
        
        if event.type == pygame.KEYDOWN:
            pressed_key = event.unicode

    SCREEN.fill(BLACK)
    GAME_STATE_VARIABLES.update(pressed_key)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
quit()