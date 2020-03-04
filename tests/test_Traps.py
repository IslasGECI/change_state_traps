import unittest
import datetime 
from change_state_traps import *


class MockObject:
    def __init__(self, effort: int):
        self.effort = effort

class TestTrap(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.simulado: MockObject = MockObject(effort = 3) 
        self.trampa: Trap = Trap(effort = 3)

    def test_calculate_effort(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        self.assertEqual(self.trampa.effort, self.simulado.effort)

if __name__ == '__main__':
    unittest.main()