import pygame
import pygame
from src.states.basestate import Base

class Start(Base):

    """ This state is active when player has entered the game for the first time. """

    def __init__(self) -> None:
        super().__init__()