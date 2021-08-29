import pygame

from Classes.bubbles import Bubble
from Classes.ball import Ball
from stats import Add_new_data, get_highScore
from datetime import datetime
from levels import level1, level2, level3
from Classes.buttons import Button

pygame.init()

#================= COLORS ====================#
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 200)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
CHOCOLATY = (210, 105, 30)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
LIGHTBLUE = (173, 216, 230)
DARKCYAN = (0, 139, 139)
#================= COLORS ===================#

#=============== GAME WINDOW =============#
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ball Breaker")
#=============== GAME WINDOW =============#

#============= Score window =================#
score_height = 50
SCORE = 0
score_color = BLACK
HIGH_SCORE = get_highScore()
NAME = ""
LEVEL = 1
#============= Score window =================#

#=============== Bubble sprite ==============#
bubbles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

bubble_height = 25
bubble_width = 50
row_count = WINDOW_HEIGHT // (bubble_height * 3)
col_count = WINDOW_WIDTH // (bubble_width + 4)

def show_bubbles(level):
    if (level == 1) : level1(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))
    elif (level == 2) : level2(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))
    elif (level == 3) : level3(row_count, col_count, bubbles, all_sprites, score_height, LIGHTBLUE, (bubble_width, bubble_height))
show_bubbles(LEVEL)
#=============== Bubble sprite ==============#

#===================== Slider =========================#
plank = pygame.sprite.GroupSingle()
slider_width = 60
slider_height = 15
slider_speed = 8
slider_direction = 0
slider = Bubble(slider_width, slider_height, GREEN)
slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
slider.rect.y = WINDOW_HEIGHT - slider_height - 5
all_sprites.add(slider)
plank.add(slider)
#===================== Slider =========================#

#==================== Ball =======================#
ball_size = 15
ball_speed = 4
ball_direction = [1, -1]
ball = Ball(ball_size, ball_size, RED)
ball.rect.x = slider.rect.x + ball_size + 2
ball.rect.y = slider.rect.y - slider_height - ball_size // 4
all_sprites.add(ball)
#==================== Ball =======================#

#============= Text =====================#
def print_text(t, color, x,y, font_size, center=True):
    font = pygame.font.SysFont("Comic sans MS", font_size)
    text = font.render(t, True, color, BLACK)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    if center : SCREEN.blit(text, (textRect[0] - textRect[2] / 2, textRect[1] - textRect[3] / 2))
    else : SCREEN.blit(text, textRect)

#============= Text =====================#

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


#================== Game State =====================#
GAME_STATE = "start"

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
        print_text("Game Over!", RED, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 72)
        print_text(f"score : {SCORE}", WHITE, 0, 10, 24, False)
        print_text(f"High Score : {HIGH_SCORE}", WHITE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100, 48)
        # print_text("press spacebar to play again", LIGHTBLUE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 200, 48)

        startbtn = Button(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 + 200, "Play Again", SCREEN, GREEN)
        endbtn =  Button(3 * WINDOW_WIDTH / 4 - 100, WINDOW_HEIGHT / 2 + 200, "Quit", SCREEN, RED)

        if (startbtn.hover()) : 
            startbtn = Button(WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 + 200, "Play Again", SCREEN, DARKGREEN)
            mouseClicked = pygame.mouse.get_pressed()
            if (mouseClicked[0]) :
                GAME_STATE ="play"
                restart()
        
        if (endbtn.hover()) : 
            endbtn = Button(3 * WINDOW_WIDTH / 4 - 100, WINDOW_HEIGHT / 2 + 200, "Quit", SCREEN, DARKRED)
            mouseClicked = pygame.mouse.get_pressed()
            if (mouseClicked[0]) : 
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Add_new_data(NAME, str(now), SCORE)
                pygame.quit()
                quit()
    elif gs == "settings":
        """ Settings for the game"""
        print_text("Click on a box to change the theme", BLUE, WINDOW_WIDTH // 2, 100, 24, True)

        board_size = 60
        s_width = 60
        s_height = 10
        bl_r = 5
        t_size = 15
        def showTheme(x, y, b_c, s_c, bl_c, t_c, text):
            back = pygame.draw.rect(SCREEN, b_c, [x, y, board_size, board_size])
            print_text(text, WHITE, back.left-16, back.top, 16, False)
            s = pygame.draw.rect(SCREEN, s_c, [x, back.bottom - s_height, s_width, s_height])
            b = pygame.draw.circle(SCREEN, bl_c, (s.center[0], s.top - bl_r), bl_r)
            t = pygame.draw.rect(SCREEN, t_c, [back.center[0], back.top + 5, t_size, t_size])
            slider.change_color(s_c)
        showTheme(40, WINDOW_HEIGHT/4, WHITE, GREEN, RED, LIGHTBLUE, "1")
#================== Game State =====================#

GAME_OVER = False
clock = pygame.time.Clock()

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