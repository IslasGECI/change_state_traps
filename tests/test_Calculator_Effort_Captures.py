import unittest
import datetime 
from change_state_traps import *


class TestCalculatorEffortCaptures(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.Esfuerzo_Capturas : Calculator_Effort_Captures = Calculator_Effort_Captures()

    def test_initialization(self):
        """
        Verifica que los objetos de las clase `Calculator_Effort_Captures` se puedan inicializar.
        """
        self.assertEqual(self.Eafuerzo_Capturas , Calculator_Effort_Captures)

if __name__ == '__main__':
    unittest.main()