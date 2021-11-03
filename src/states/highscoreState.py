import pygame
from src.states.basestate import Base

class Highscore(Base):

    """ This state is active after the player clicks highscore button in startscreen. """

    def __init__(self) -> None:
        super().__init__()