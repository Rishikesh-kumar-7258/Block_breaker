class GameStateChanger:
    """
    This class will help in managing the differnt states in the game.
    """

    def __init__(self, states=None) -> None:
        
        self.states = states
        self.current = None
    
    def change(self, state, **params):
        """" Used when state needs to be changed """

        # checking if the passed states is in the current state or not
        if not state in self.states:
            return

        # leaving the current state
        self.current.leave()

        # Making the passed state as the current state
        self.current = self.states[state]
        self.current.enter()
    
    def render(self):
        """ redering the current state """

        self.current.render()
    
    def update(self, param):
        """ updating the current state """

        self.current.update(param)