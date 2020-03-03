import unittest
import datetime 
from change_state_traps import calculate_time_interval_day

class TestCalculateTimeIntervalDay(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.date1 = datetime.datetime(2017, 6, 21, 18, 25, 30)
        self.date2 = datetime.datetime(2017, 5, 16, 8, 21, 10)  

    def test_calculate_time_interval_day(self):
        """
        Prueba que calcula la diferencia en días de dos fechas
        """
        interval = calculate_time_interval_day(self.date1, self.date2)
        self.assertEqual(interval, 36)

if __name__ == '__main__':
    unittest.main()