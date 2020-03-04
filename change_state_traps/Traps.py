import datetime 

class Trap:
    def __init__(self, effort : int, state : str, last_change : datetime):
        self.effort : int = effort
        self.__state : str = state
        self.__last_change : datetime = last_change

    @property
    def state(self):
        return(self.__state)

    @property
    def last_change(self):
        return(self.__last_change)

    def update(self, new_state : str, new_date : datetime):
        self.__state = new_state
        self.__last_change = new_date
