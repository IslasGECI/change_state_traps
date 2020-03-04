class Trap:
    def __init__(self, state: str, days: int):
        self.days: int = days
        self.state: str = state

def calculate_effort_from_state(Trampa: Trap):
    if Trampa.state == "A":
        return(Trampa.days)
    else:
        return(0)