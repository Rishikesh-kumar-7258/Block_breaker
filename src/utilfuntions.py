import pygame
from src.objects import PARTICLE

# displaying text on the screen
def Write(screen, text, x, y, size, color, center=False) -> None:
    """ This function will render text on screen"""

    font = pygame.font.SysFont(None, size)
    text = font.render(text, False, color)
    rect = text.get_rect()
    if (center):
        rect.center = (x, y)
    else :
        rect.x = x
        rect.y = y
    screen.blit(text, rect)

def update_score(player_name, player_score):

    file = open("scores.csv", 'a')

    file.write(player_name + ',' + str(player_score) + '\n')
        
def get_score():
    file = open("scores.csv", 'r')

    scores = {}
    i = 0
    for line in file:
        i += 1
        if i == 1:
            continue
        line = line.strip()
        player, score = line.split(',')
        scores[player] = int(score)

    file.close()
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def collision(obj1 : dict, obj2 : dict) -> bool:
    """ detects collision between 2 objects and returns some properties in list """

    if (obj1['x'] + obj1['width'] /2 < obj2['x'] - obj2['width'] / 2 or
        obj1['x'] - obj1['width'] / 2 > obj2['x'] + obj2['width'] / 2 or
        obj1['y'] + obj1['height'] < obj2['y'] or
        obj1['y'] > obj2['y'] + obj2['height']):
        return False

    return True