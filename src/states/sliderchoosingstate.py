import pygame
from src.states.basestate import Base

class SliderChoosingg(Base):

    """ This state is active after the start state or before the play state. """

    def __init__(self) -> None:
        super().__init__()