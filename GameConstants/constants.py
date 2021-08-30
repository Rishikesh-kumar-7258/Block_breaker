import pygame
from Classes.bubbles import Bubble

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


#=============== SCORE WINDOW =============#
score_height = 50
SCORE = 0
score_color = BLACK
#=============== SCORE WINDOW =============#

#=============== SLIDER =============#
slider_width = 60
slider_height = 15
slider_speed = 8
slider_direction = 0
slider = Bubble(slider_width, slider_height, GREEN)
slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
slider.rect.y = WINDOW_HEIGHT - slider_height - 5
#=============== SLIDER =============#

#=============== BALL =============#
ball_size = 15
ball_speed = 4
#=============== BALL =============#
