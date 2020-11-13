import datetime

from change_state_traps import *


class MockObject:
    def __init__(self, effort: int, capture: int, state: str, last_change: datetime):
        self.changed_effort = 6
        self.changed_last_change: datetime = datetime.datetime(2020, 5, 20)
        self.changed_state: str = "D"
        self.effort = effort
        self.capture = capture
        self.last_change: datetime = last_change
        self.state: str = state


ultimo_cambio = datetime.datetime(2020, 5, 17)
argumentos = {"effort": 3, "capture": 2, "state": "A", "last_change": ultimo_cambio}
simulado: MockObject = MockObject(**argumentos)
trampa: Trap = Trap(**argumentos)


def test_verifies_capture():
    """
    Verifica que los objetos de las clase `Trap` se construyan de manera correcta e su propiedad `effort`.
    """
    assert trampa.capture == simulado.capture


def test_verifies_effort():
    """
    Verifica que los objetos de las clase `Trap` se construyan de manera correcta e su propiedad `effort`.
    """
    assert trampa.effort == simulado.effort


def test_verifies_state():
    """
    Verifica que los objetos de las clase `Trap` se construyan de manera correcta en su propiedad `state`.
    """
    assert trampa.state == simulado.state


def test_verifies_last_change():
    """
    Verifica que los objetos de las clase `Trap` se construyan de manera correcta en su propiedad `state`.
    """
    assert trampa.last_change == simulado.last_change


def test_update_trap():
    """
    Verifica que los objetos de las clase `Trap` se puedan actualizar cuando exista un cambio en su estado.
    """
    trampa.update(new_state="D", new_date=datetime.datetime(2020, 5, 20))
    assert trampa.state == "D"
    assert trampa.last_change == datetime.datetime(2020, 5, 20)
    esfuerzo_del_17_al_19 = 3
    assert trampa.effort == simulado.effort + esfuerzo_del_17_al_19
    trampa.update(new_state="A", new_date=datetime.datetime(2020, 5, 27))
    assert trampa.effort == simulado.effort + esfuerzo_del_17_al_19
    esfuerzo_del_27_al_29 = 3
    trampa.update(new_state="X", new_date=datetime.datetime(2020, 5, 29))
    assert trampa.effort == simulado.effort + esfuerzo_del_17_al_19 + esfuerzo_del_27_al_29
    assert trampa.capture == simulado.capture + 1
