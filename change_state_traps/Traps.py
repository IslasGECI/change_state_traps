import datetime 

class Trap:
    def __init__(self, effort : int, state : str, last_change : datetime):
        self.effort : int = effort
        self.state : str = state
        self.last_change : datetime = last_change