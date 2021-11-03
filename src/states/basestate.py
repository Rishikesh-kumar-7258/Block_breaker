class Base:
    """ This is the template for all the other classes """

    def __init__(self) -> None:
        """ constructor class """

        pass
    def enter(self, entity) -> None:
        """ This is the enter function. Called first when state is changed """

        pass
    
    def leave(self) -> None:
        """ This is the leave function. Used during changing state."""
    
    def update(self, entity) -> None:
        """ This is the update function. Called every frame """

        pass

    def render(self) -> None:
        """ This will render the current state on the screen """

        pass