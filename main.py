import pygame
from bubbles import Bubble
from ball import Ball
from stats import Add_new_data
from datetime import datetime
pygame.init()

#================= COLORS ====================#
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
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
HIGH_SCORE = 0
NAME = ""
#============= Score window =================#

#=============== Bubble sprite ==============#
bubbles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

bubble_size = 25
row_count = WINDOW_HEIGHT // (bubble_size * 3)
col_count = WINDOW_WIDTH // (bubble_size + 4)

for i in range(row_count):
    for j in range(col_count-1):
        # if (j&1 == 1) : continue
        bubble = Ball(bubble_size, bubble_size, DARKCYAN)
        bubble.rect.x = j*(bubble_size+5) + 10
        bubble.rect.y = i*(bubble_size+5) + score_height + 2
        bubbles.add(bubble)
        all_sprites.add(bubble)
#=============== Bubble sprite ==============#

#===================== Slider =========================#
plank = pygame.sprite.GroupSingle()
slider_width = 60
slider_height = 15
slider_speed = 5
slider_direction = 0
slider = Bubble(slider_width, slider_height, GREEN)
slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
slider.rect.y = WINDOW_HEIGHT - slider_height - 5
all_sprites.add(slider)
plank.add(slider)
#===================== Slider =========================#

#==================== Ball =======================#
ball_size = 20
ball_speed = 4
ball_direction = [1, -1]
ball = Ball(ball_size, ball_size, RED)
ball.rect.x = slider.rect.x + ball_size + 2
ball.rect.y = slider.rect.y - slider_height - ball_size // 4
all_sprites.add(ball)
#==================== Ball =======================#

#============= Text =====================#
font = pygame.font.SysFont("Roboto", 55)
name = pygame.font.SysFont("Roboto", 25)
def print_text(t, color, x,y):
    text = font.render(t, True, color, BLACK)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    SCREEN.blit(text, textRect)

def input_name():
    global NAME
    def print_something(t, x, y):
        text = name.render(t, True, GREEN, BLACK)
        textRect = text.get_rect()
        textRect.x = x
        textRect.y = y
        SCREEN.blit(text, textRect)
    print_something(f"Enter your Name: {NAME}", WINDOW_WIDTH // 4, WINDOW_HEIGHT//4)

#============= Text =====================#

def restart():
    """
        starting a new game
    """
    ball.rect.x = slider.rect.x + ball_size + 2
    ball.rect.y = slider.rect.y - slider_height - ball_size // 4 
    slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
    slider.rect.y = WINDOW_HEIGHT - slider_height - 5
    SCORE = 0
    ball_direction = [1, -1]
    return


#================== Game State =====================#
GAME_STATE = "start"
def state_play(gs):
    """
        Takes game state and plays the game accordingly
    """
    global GAME_STATE
    if gs == "start":
        
        print_text("Bubble Shooter", LIGHTBLUE, WINDOW_WIDTH // 2 - 110, WINDOW_HEIGHT // 2 - 55)
        input_name()
        print_text("press Tab to play", LIGHTBLUE, WINDOW_WIDTH // 2 - 220, WINDOW_HEIGHT // 2 + 55)

    elif gs == "play":

        global slider_direction
        #===== moving the slider =========#
        slider.move(slider_speed, slider_direction)
        if (slider.rect.x <= 0 or slider.rect.x >= WINDOW_WIDTH - slider_width):
            slider_direction = 0
        #===== moving the slider =========#

        #========= moving the ball =============#
        ball.move(ball_speed*ball_direction[0], ball_speed*ball_direction[1])
        if (ball.rect.x <= 0) or (ball.rect.x >= WINDOW_WIDTH - ball_size) : ball_direction[0] *= -1
        if (ball.rect.y <= score_height) : ball_direction[1] *= -1
        if (ball.rect.y >= WINDOW_HEIGHT):
            GAME_STATE = "over"
        #========= moving the ball =============#

        #================ collision detection ===============#
        slider_collision = pygame.sprite.spritecollide(ball, plank, False, pygame.sprite.collide_mask)
        for s in slider_collision:
            if (ball.rect.x > s.rect.x and ball.rect.x < s.rect.x + slider_width):
                ball_direction[1] *= -1
            elif (ball.rect.y > s.rect.y and ball.rect.y < s.rect.y + slider_height):
                ball_direction[0] *= -1

        shooted_bubbles = pygame.sprite.spritecollide(ball, bubbles, True, pygame.sprite.collide_mask)
        for b in shooted_bubbles:
            global SCORE
            if (ball.rect.x > b.rect.x and ball.rect.x < b.rect.x + bubble_size):
                ball_direction[1] *= -1
            elif (ball.rect.y > b.rect.y and ball.rect.y < b.rect.y + bubble_size):
                ball_direction[0] *= -1
            SCORE += 1
        #================ collision detection ===============#
        
        pygame.draw.rect(SCREEN, score_color, [0, 0, WINDOW_WIDTH, score_height])
        print_text(f"score : {SCORE}", WHITE, 0, 10)
        all_sprites.update()
        all_sprites.draw(SCREEN)
    elif gs == "over":
        print_text("Game Over!", RED, WINDOW_WIDTH // 2 - 110, WINDOW_HEIGHT // 2)
        print_text(f"score : {SCORE}", WHITE, 0, 10)
        print_text(f"High Score : {HIGH_SCORE}", WHITE, WINDOW_WIDTH // 2 - 110, WINDOW_HEIGHT // 2 + 55)
        print_text("press spacebar to play again", LIGHTBLUE, WINDOW_WIDTH // 2 - 220, WINDOW_HEIGHT // 2 + 220)
        restart()
        # currTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Add_new_data(NAME, currTime, SCORE)


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
                    GAME_STATE = "play"
                else : NAME += event.unicode
            if GAME_STATE == "over":
                if event.key == pygame.K_SPACE:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    Add_new_data(NAME, str(now), SCORE)
                    GAME_STATE = "play"
            if event.key == pygame.K_LEFT and slider.rect.x > 0:
                slider_direction = -1
            elif event.key == pygame.K_RIGHT and slider.rect.x < WINDOW_WIDTH - slider_width:
                slider_direction = 1

        elif event.type == pygame.KEYUP:
            slider_direction = 0

    SCREEN.fill(BLACK)
    state_play(GAME_STATE)
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()
quit()