import pygame
from bubbles import Bubble
from ball import Ball
pygame.init()

#================= COLORS ====================#
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CHOCOLATY = (210, 105, 30)
GRAY = (128, 128, 128)
#================= COLORS ===================#

#=============== GAME WINDOW =============#
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bubble Shooter")
#=============== GAME WINDOW =============#

#=============== Bubble sprite ==============#
bubbles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

bubble_size = 25
row_count = WINDOW_HEIGHT // (bubble_size * 3)
col_count = WINDOW_WIDTH // (bubble_size + 4)

for i in range(row_count):
    for j in range(col_count-1):
        bubble = Bubble(bubble_size, bubble_size, CHOCOLATY)
        bubble.rect.x = j*(bubble_size+5) + 10
        bubble.rect.y = i*(bubble_size+5) + 5
        bubbles.add(bubble)
        all_sprites.add(bubble)
#=============== Bubble sprite ==============#

#===================== Slider =========================#
slider_width = 60
slider_height = 15
slider_speed = 5
slider_direction = 0
slider = Bubble(slider_width, slider_height, GREEN)
slider.rect.x = (WINDOW_WIDTH // 2) - (slider_width // 2)
slider.rect.y = WINDOW_HEIGHT - slider_height - 5
all_sprites.add(slider)
#===================== Slider =========================#

#==================== Moving Ball =======================#
ball_radius = 20
# ball_width = 20
ball_speed = 10
ball = Ball(ball_radius, RED)
ball.rect.x = slider.rect.x + slider_width // 2
ball.rect.y = slider.rect.y - slider_height // 2 - ball_radius
all_sprites.add(ball)
#==================== Moving Ball =======================#

GAME_OVER = False
clock = pygame.time.Clock()

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and slider.rect.x > 0:
                slider_direction = -1
            elif event.key == pygame.K_RIGHT and slider.rect.x < WINDOW_WIDTH - slider_width:
                slider_direction = 1
        elif event.type == pygame.KEYUP:
            slider_direction = 0
    
    #===== moving the slider =========#
    slider.move(slider_speed, slider_direction)
    if (slider.rect.x <= 0 or slider.rect.x >= WINDOW_WIDTH - slider_width):
        slider_direction = 0
    #===== moving the slider =========#

    SCREEN.fill(GRAY)
    all_sprites.update()
    all_sprites.draw(SCREEN)
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()
quit()