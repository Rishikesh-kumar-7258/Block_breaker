import pygame

from src.spritesheet import SpriteSheet, balls, blocks, sliders
pygame.init()

# parameters for the screen
screen_width = 800
screen_height = 600

# Setting up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")
pygame.display.set_icon(pygame.image.load("images/logo.png"))

# differenst states
gameStates = {}

# spritesheet
sprite = SpriteSheet("images/spritesheet.png")
block_array = blocks(sprite)
ball_array = balls(sprite)
slider_array = sliders(sprite)

# setting up the game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing the screen
    screen.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
quit()