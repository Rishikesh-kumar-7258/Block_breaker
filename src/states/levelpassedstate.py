import pygame
from src.states.basestate import Base

class LevelPassed(Base):

    """ This state is active when player has passed the current level. """

    def __init__(self) -> None:
        super().__init__()