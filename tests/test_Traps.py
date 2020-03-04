import unittest
import datetime 
from change_state_traps import *


class MockObject:
    def __init__(self, effort: int, state : str, last_change : datetime):
        self.effort = effort
        self.state : str = state
        self.changed_state : str = "D"
        self.last_change : datetime = last_change

class TestTrap(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        ultimo_cambio = datetime.datetime(2020, 5, 17)
        self.simulado: MockObject = MockObject(effort = 3, state = "A", last_change = ultimo_cambio) 
        self.trampa: Trap = Trap(effort = 3, state = "A", last_change = ultimo_cambio)

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

    def test_verifies_changed_state(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta en su propiedad `state`. 
        """
        self.trampa.state = "D"
        self.assertEqual(self.trampa.state, self.simulado.changed_state)

if __name__ == '__main__':
    unittest.main()