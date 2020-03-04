import unittest
import datetime 
from change_state_traps import *


class MockObject:
    def __init__(self, effort: int, state : str, last_change : datetime):
        self.changed_effort = 6
        self.changed_last_change : datetime = datetime.datetime(2020, 5, 20)
        self.changed_state : str = "D"
        self.effort = effort
        self.last_change : datetime = last_change
        self.state : str = state

class TestTrap(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        ultimo_cambio = datetime.datetime(2020, 5, 17)
        argumentos = {"effort" : 3, "state" : "A", "last_change" : ultimo_cambio}
        self.simulado: MockObject = MockObject(**argumentos) 
        self.trampa: Trap = Trap(**argumentos)

    def test_verifies_effort(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta e su propiedad `effort`. 
        """
        self.assertEqual(self.trampa.effort, self.simulado.effort)

    def test_verifies_state(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta en su propiedad `state`. 
        """
        self.assertEqual(self.trampa.state, self.simulado.state)

    def test_verifies_last_change(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta en su propiedad `state`. 
        """
        self.assertEqual(self.trampa.last_change, self.simulado.last_change)

    def test_update_trap(self):
        """
        Verifica que los objetos de las clase `Trap` se puedan actualizar cuando exista un cambio en su estado.
        """
        self.trampa.update(new_state = "D", new_date = datetime.datetime(2020, 5, 20))
        self.assertEqual(self.trampa.state, "D")
        self.assertEqual(self.trampa.last_change, datetime.datetime(2020, 5, 20))
        self.assertEqual(self.trampa.effort, self.simulado.effort + 3)
        self.trampa.update(new_state = "A", new_date = datetime.datetime(2020, 5, 27))
        self.assertEqual(self.trampa.effort, self.simulado.effort + 3)
        self.trampa.update(new_state = "X", new_date = datetime.datetime(2020, 5, 29))
        self.assertEqual(self.trampa.effort, self.simulado.effort + 5)

if __name__ == '__main__':
    unittest.main()