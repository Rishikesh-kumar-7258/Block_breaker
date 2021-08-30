import pygame

from Classes.bubbles import Bubble
from Classes.ball import Ball
from stats import *
from datetime import datetime
from Classes.buttons import Button
from Classes.themeboard import Themeboard
from GameConstants.constants import *
from GameConstants.variables import *
from Functions.textfunctions import *

# from statechanger import StateMachine
# from States.start import Start

pygame.init()

show_bubbles(LEVEL)

def restart():
    """
        starting a new game
    """
    global GAME_STATE, SCORE, ball, slider, bubbles, plank, all_sprites
    bubbles.empty()
    plank.empty()
    all_sprites.empty()
    slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
    slider.rect.y = WINDOW_HEIGHT - slider_height - 5
    ball.rect.x = slider.rect.x + ball_size + 2
    ball.rect.y = slider.rect.y - slider_height - ball_size // 4
    SCORE = 0
    ball_direction = [1, -1]
    all_sprites.add(slider)
    all_sprites.add(ball)
    plank.add(slider)
    show_bubbles(LEVEL)
    return

# states = {
#         "play" : Start()
#     }
# GAME_STATE = StateMachine(states)

# GAME_STATE.change("play")

#================== Game State =====================#
def state_play(gs):
    """
        Takes game state and plays the game accordingly
    """
    global slider_direction, GAME_STATE, LEVEL, SCORE, HIGH_SCORE
    if gs == "start":
        print_text("Bubble Shooter", LIGHTBLUE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 72)
        print_text(f"Enter your Name: {NAME}", GREEN, WINDOW_WIDTH / 2, WINDOW_HEIGHT/2 - 100, 20)
        # print_text("press Tab to play", LIGHTBLUE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100, 48)

        # Button(x, y, text, screen, color, hcolor)
        startbtn = Button(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 + 200, "Play", SCREEN, GREEN)
        setbtn = Button(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2 + 200, "Settings", SCREEN, BLUE)
        endbtn =  Button(3 * WINDOW_WIDTH / 4 - 100, WINDOW_HEIGHT / 2 + 200, "Quit", SCREEN, RED)

        if (startbtn.hover()) : 
            startbtn = Button(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 + 200, "Play", SCREEN, DARKGREEN)
            mouseClicked = pygame.mouse.get_pressed()
            if (mouseClicked[0]) : GAME_STATE ="play"

        if (setbtn.hover()) : 
            setbtn = Button(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2 + 200, "Settings", SCREEN, DARKBLUE)
            mouseClicked = pygame.mouse.get_pressed()
            if (mouseClicked[0]) : GAME_STATE ="settings"
        
        if (endbtn.hover()) : 
            endbtn = Button(3 * WINDOW_WIDTH / 4 - 100, WINDOW_HEIGHT / 2 + 200, "Quit", SCREEN, DARKRED)
            mouseClicked = pygame.mouse.get_pressed()
            if (mouseClicked[0]) : 
                pygame.quit()
                quit()

    elif gs == "play":
        #===== moving the slider =========#
        slider.move(slider_speed, slider_direction)
        if (slider.rect.x <= 0 or slider.rect.x >= WINDOW_WIDTH - slider_width):
            slider_direction = 0
        #===== moving the slider =========#

        #========= moving the ball =============#
        ball.move(ball_speed*ball_direction[0], ball_speed*ball_direction[1])
        if (ball.rect.x <= 0) : ball_direction[0] = 1
        elif ball.rect.x >= WINDOW_WIDTH - ball_size : ball_direction[0] = -1

        if (ball.rect.y <= score_height) : ball_direction[1] = 1
        if (ball.rect.y >= WINDOW_HEIGHT):
            HIGH_SCORE = SCORE if HIGH_SCORE < SCORE else HIGH_SCORE
            GAME_STATE = "over"
        #========= moving the ball =============#

        #================ collision detection ===============#
        slider_collision = pygame.sprite.spritecollide(ball, plank, False, pygame.sprite.collide_mask)
        for s in slider_collision:
            if (ball.rect.x > s.rect.x - ball_size / 2 and ball.rect.x < s.rect.x + slider_width + ball_size / 2):
                if (ball.rect.y <= slider.rect.y - ball_size / 2) : ball_direction[1] = -1
                else : ball_direction[1] = 1
            elif (ball.rect.y > s.rect.y - ball_size / 2 and ball.rect.y < s.rect.y + slider_height + ball_size / 2):
                if (ball.rect.x <= slider.rect.x - ball_size/2) : ball_direction[0] = -1
                else : ball_direction[0] = 1

        shooted_bubbles = pygame.sprite.spritecollide(ball, bubbles, True, pygame.sprite.collide_mask)
        if len(bubbles) == 0 : # IF THE PLAYER SMASHES ALL THE BLOCKS INCREASE THE LEVEL
            LEVEL += 1
            GAME_STATE = "over"
        for b in shooted_bubbles:
            if (ball.rect.x > b.rect.x and ball.rect.x < b.rect.x + bubble_width):
                ball_direction[1] *= -1
            elif (ball.rect.y > b.rect.y and ball.rect.y < b.rect.y + bubble_height):
                ball_direction[0] *= -1
            SCORE += 1
        #================ collision detection ===============#
        
        pygame.draw.rect(SCREEN, score_color, [0, 0, WINDOW_WIDTH, score_height])
        print_text(f"score : {SCORE}", WHITE, 0, 10, 24, False)
        all_sprites.update()
        all_sprites.draw(SCREEN)
    elif gs == "over":
        if (len(bubbles) == 0) :
            print_text("Congratulations!", GREEN, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100, 72)
            print_text("You passed the level", GREEN, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 36)
        else : print_text("Game Over!", RED, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 72)
        print_text(f"score : {SCORE}", WHITE, 0, 10, 24, False)
        print_text(f"High Score : {HIGH_SCORE}", WHITE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100, 48)
        # print_text("press spacebar to play again", LIGHTBLUE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 200, 48)

        s_text = "Next Level" if len(bubbles) == 0 else "Play Again"
        startbtn = Button(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 + 200, s_text, SCREEN, GREEN)
        endbtn =  Button(3 * WINDOW_WIDTH / 4 - 100, WINDOW_HEIGHT / 2 + 200, "Quit", SCREEN, RED)

        if (startbtn.hover()) : 
            startbtn = Button(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 + 200, s_text, SCREEN, DARKGREEN)
        if (startbtn.clicked()):
            GAME_STATE ="play"
            restart()
        
        if (endbtn.hover()) : 
            endbtn = Button(3 * WINDOW_WIDTH / 4 - 100, WINDOW_HEIGHT / 2 + 200, "Quit", SCREEN, DARKRED)
            mouseClicked = pygame.mouse.get_pressed()
        if (endbtn.clicked()):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Add_new_data(NAME, str(now), SCORE)
            pygame.quit()
            quit()
                
    elif gs == "settings":
        """ Settings for the game"""
        print_text("Click on a box to change the theme", BLUE, WINDOW_WIDTH // 2, 100, 24, True)
        
        t1 = Themeboard(40, WINDOW_HEIGHT/4, WHITE, GREEN, RED, LIGHTBLUE)

        backbtn = Button(WINDOW_WIDTH // 2 - 100, 3*WINDOW_HEIGHT//4, "Back", SCREEN, BLUE)
        if backbtn.hover() : backbtn = Button(WINDOW_WIDTH // 2 - 100, 3*WINDOW_HEIGHT//4, "Back", SCREEN, DARKBLUE)
        if (backbtn.clicked()):
            GAME_STATE = "start"
#================== Game State =====================#

while not GAME_OVER:

    for event in pygame.event.get():

        #quitting the game with red cross mark on the top right corner
        if event.type == pygame.QUIT:
            if GAME_STATE == "over":
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Add_new_data(NAME, str(now), SCORE)
            GAME_OVER = True
        
        #If any key is pressed
        if event.type == pygame.KEYDOWN:
            if GAME_STATE == "start":
                if event.key == pygame.K_TAB:
                    # GAME_STATE = "play"
                    pass
                else : 
                    if event.key == pygame.K_BACKSPACE :
                        NAME = NAME[:-1]
                    elif event.unicode == '\r' : pass
                    else : NAME += event.unicode
            if GAME_STATE == "over":
                if event.key == pygame.K_SPACE:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    Add_new_data(NAME, str(now), SCORE)
                    restart()
                    GAME_STATE = "play"
            if event.key == pygame.K_LEFT and slider.rect.x > 0:
                slider_direction = -1
            elif event.key == pygame.K_RIGHT and slider.rect.x < WINDOW_WIDTH - slider_width:
                slider_direction = 1

        if event.type == pygame.KEYUP:
            slider_direction = 0

    SCREEN.fill(BLACK)
    state_play(GAME_STATE)
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()
quit()