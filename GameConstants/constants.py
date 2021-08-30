import pygame
from Classes.bubbles import Bubble
from Classes.ball import Ball

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
LOGO = pygame.image.load("Images/logo.png")
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ball Breaker")
pygame.display.set_icon(LOGO)
GAME_STATE = "start"
GAME_OVER = False
clock = pygame.time.Clock()
#=============== GAME WINDOW =============#


#=============== SCORE WINDOW =============#
score_height = 50
SCORE = 0
score_color = BLACK
#=============== SCORE WINDOW =============#

#=============== SPRITE GROUPS =============#
bubbles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
#=============== SPRITE GROUPS =============#

#=============== SLIDER =============#
slider_width = 60
slider_height = 15
slider_speed = 8
slider_direction = 0
slider = Bubble(slider_width, slider_height, GREEN)
slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
slider.rect.y = WINDOW_HEIGHT - slider_height - 5
plank = pygame.sprite.GroupSingle()
all_sprites.add(slider)
plank.add(slider)
#=============== SLIDER =============#

#=============== BALL =============#
ball_size = 15
ball_speed = 4
ball = Ball(ball_size, ball_size, RED)
ball.rect.x = slider.rect.x + ball_size + 2
ball.rect.y = slider.rect.y - slider_height - ball_size // 4
all_sprites.add(ball)
#=============== BALL =============#

#=============== BUBBLE SPRITE =============#
bubble_height = 25
bubble_width = 50
row_count = WINDOW_HEIGHT // (bubble_height * 3)
col_count = WINDOW_WIDTH // (bubble_width + 4)
#=============== BUBBLE SPRITE =============#