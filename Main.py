import pygame
pygame.init()

#importing out custom make box class
import boxClass

# defining different states
state = {
    "start": 1,
    "play": 2,
    "playing" : 3,
    "game_over": 4,
}

# difining different colors
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (64, 64, 64),
    "chocolaty" : (210, 105, 30)
}

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
# GAME_OVER = False
GAME_STATE = state["playing"]

# making the game window
GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BUBBLE SHOOTER")

# Initialising our fonts
font = pygame.font.SysFont("none", 55)

# setting for our fps
fps = 30
clock = pygame.time.Clock()

# function to render text on screen


def text_display(text, color, background, x, y):
    t = font.render(text, True, color, background)
    GAME_WINDOW.blit(t, [x, y])


class Button:
    """
        creating a clickable buttons
    """

    def __init__(self, text="I am a button", color=colors["white"], background=colors["black"], x=0, y=0, width=90, height=50):
        self.text = text
        self.color = color
        self.background = background
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        pygame.draw.rect(GAME_WINDOW, self.background,
                        (self.x, self.y, self.width, self.height))
        text_display(self.text, self.color, self.background, self.x, self.y)
    
    def Collides(self, x, y):
        if (x >= self.x and x <= self.x + self.width) and (y >= self.y and y <= self.y + self.height):
            return True
        else : return False

    def Click(self):
        global GAME_STATE
        GAME_STATE = state["play"]
        # print(self.x, self.x+self.width, self.y, self.y+self.height)

#creating a button 
BUTTON = Button("Start", x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT//2)

def displayScreen(s):
    """
    Creating a function which will render the game according to the play state it is in
    """


    GAME_WINDOW.fill(colors["gray"])

    if s == state["start"]:

        text_display("BUBBLE SHOOTER", colors["green"], colors["blue"],
                    WINDOW_WIDTH//2 - 110, WINDOW_HEIGHT//2 - 55)
        BUTTON.Show()

    elif s == state["play"]:

        text_display("Press space to start",
                    colors["green"], colors["blue"],  WINDOW_WIDTH//2 - 110, WINDOW_HEIGHT//2 - 55)
    elif s == state["playing"]:
        rows = WINDOW_HEIGHT //( boxClass.HEIGHT * 4)
        cols = WINDOW_WIDTH // boxClass.WIDTH
        boxClass.Pattern(1, rows, cols, GAME_WINDOW, colors["chocolaty"])
        


    pygame.display.update()



while not GAME_STATE == state["game_over"]:

    """
        Game loop
    """

    clock.tick(fps)
    displayScreen(GAME_STATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATE = state["game_over"]

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()

            if GAME_STATE==state["start"] and BUTTON.Collides(x,y):
                BUTTON.Click()

        if event.type == pygame.KEYDOWN:
            if event.unicode == ' ' and GAME_STATE == state["play"]:
                GAME_STATE = state["playing"]

#quitting the game
pygame.quit()
quit()