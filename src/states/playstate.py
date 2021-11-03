import pygame
from src.states.basestate import Base

class Play(Base):

    """ This state is active when player is currently playing the game. """

    def __init__(self) -> None:
        super().__init__()
