def calculate_effort_from_state(Trampa):
    if Trampa.state == "A":
        return Trampa.days
    else:
        return 0
