import pygame

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