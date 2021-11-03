import pygame
from src.states.basestate import Base

class GameOver(Base):

    """ This state is active when game is over. """

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        pass