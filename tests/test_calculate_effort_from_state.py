import unittest
import datetime 
from change_state_traps import calculate_effort_from_state

class TestCalculateEffortFromState(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.state_actived : str = "A"
        self.state_deacatived : str = "D"
        self.days : int = 7

    def test_calculate_effort(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        effort = calculate_effort_from_state(self)
        self.assertEqual(effort, self.days)

if __name__ == '__main__':
    unittest.main()