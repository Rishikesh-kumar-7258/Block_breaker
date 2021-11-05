import pygame
from pygame.constants import SRCALPHA


class SpriteSheet:
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name) -> None:
        """ Constructor. Pass in the file name of the sprite sheet. """

        self.file_name = file_name
        self.sprite_sheet = pygame.image.load(self.file_name).convert()
    
    def make_sprite(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        sprite = pygame.Surface([width, height]).convert()

        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        sprite.set_colorkey(pygame.Color(255, 255, 255))

        return sprite
    
def blocks(spritesheet) -> list():
    """ Makes and returns the block array """

    block_array = []

    for i in range(4):
        block_array.append(spritesheet.make_sprite(i * 80, 0, 80, 20))

    return block_array

def sliders(spritesheet) -> list():
    """ Makes and returns the slider list """

    slider_array = []

    for i in range(3):
        slider_array.append(spritesheet.make_sprite(i * 100, 20, 100, 20))
    
    return slider_array

def balls(spritesheet) -> list():
    """ Makes and returns the ball list """

    ball_array = []

    for i in range(3):
        ball_array.append(spritesheet.make_sprite(i * 16, 40, 16, 16))

    return ball_array

def hearts(spritesheet) -> list():
    """ Makes and returns the hearts list """

    heart_array = []

    for i in range(2):
        heart_array.append(spritesheet.make_sprite(i * 20 + 60, 40, 20, 20))

    return heart_array

def buttons(spritesheet) -> list():
    """ Makes and returns the button list """

    button_array = []

    for i in range(4):
        button_array.append(spritesheet.make_sprite(i * 20 + 100, 40, 20, 20))

    return button_array