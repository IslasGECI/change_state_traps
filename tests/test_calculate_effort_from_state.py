import unittest
import datetime
from change_state_traps import *


class MockObject:
    def __init__(self, state: str, days: int):
        self.days: int = days
        self.state: str = state


class TestCalculateEffortFromState(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.activated = "A"
        self.deactivated = "D"
        self.weak = 7
        self.month = 30
        self.trampa1: MockObject = MockObject(state=self.activated, days=self.weak)
        self.trampa2: MockObject = MockObject(state=self.activated, days=self.month)
        self.trampa3: MockObject = MockObject(state=self.deactivated, days=self.month)

    def test_calculate_effort(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        effort = calculate_effort_from_state(self.trampa1)
        self.assertEqual(effort, self.weak)

    def test_calculate_effort_2(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        effort = calculate_effort_from_state(self.trampa2)
        self.assertEqual(effort, self.month)

    def test_calculate_effort_3(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        effort = calculate_effort_from_state(self.trampa3)
        self.assertEqual(effort, 0)


if __name__ == "__main__":
    unittest.main()
