import pygame
from random import randint

from src.objects import BLOCK

def level(screen, level) -> list():
    """ This will make a list of blocks and return """

    blocks_arr = []

    width = screen.get_width()
    height = screen.get_height()

    rows = 5
    cols = width // 80

    for i in range(rows):
        for j in range(cols):
            block = BLOCK.copy()
            block['x'] = j*80
            block['y'] = height / 10 + i*25 + 10
            block['number'] = randint(0, 3)
            blocks_arr.append(block)
    
    return blocks_arr