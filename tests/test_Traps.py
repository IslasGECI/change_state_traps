import unittest
import datetime 
from change_state_traps import *


class MockObject:
    def __init__(self):
        pass

class TestTrap(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.simulado: MockObject = MockObject() 
        self.trampa: Trap = Trap()

    def test_calculate_effort(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        self.assertEqual(self.trampa, self.simulado)

if __name__ == '__main__':
    unittest.main()