import unittest
import datetime 
from change_state_traps import *


class TestCalculatorEffortCaptures(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.Esfuerzo_Capturas : Calculator_Effort_Captures = Calculator_Effort_Captures()
        ultimo_cambio : datetime.datetime = datetime.datetime(2020, 5, 17)
        self.dictionary : dict = {"effort" : [30, 40], "state" : ["A", "A"], "last_change" : [ultimo_cambio, ultimo_cambio]}
        self.dataframe : pd.DataFrame = pd.DataFrame.from_dict(self.dictionary)

    def test_initialization(self):
        """
        Verifica que los objetos de las clase `Calculator_Effort_Captures` se puedan inicializar.
        """
        self.assertEqual(self.Esfuerzo_Capturas , Calculator_Effort_Captures)
        self.Esfuerzo_Capturas.init(self.dataframe)
        self.assertEqual(self.Esfuerzo_Capturas.effort , sum(self.dictionary['effort']))


if __name__ == '__main__':
    unittest.main()