import datetime 

class Trap:
    def __init__(self, effort : int, state : str, last_change : datetime):
        self.effort : int = effort
        self.__state : str = state
        self.last_change : datetime = last_change

    @property
    def state(self):
        return(self.__state)

    @state.setter
    def state(self, new_state : str):
        self.__state = new_state