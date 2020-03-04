import unittest
import datetime 
from change_state_traps import *


class MockObject:
    def __init__(self, effort: int, state : str):
        self.effort = effort
        self.state : str = state

class TestTrap(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.simulado: MockObject = MockObject(effort = 3, state = "A") 
        self.trampa: Trap = Trap(effort = 3, state = "A")

    def test_verifies_effort(self):
        """
        Verifica que los objetos de las clase `Trap` se construyan de manera correcta e su propiedad `effort`. 
        """
        self.assertEqual(self.trampa.effort, self.simulado.effort)

if __name__ == '__main__':
    unittest.main()