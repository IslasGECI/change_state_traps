import unittest
import datetime
import pandas as pd
from change_state_traps import *


class TestRowDataframe2Dictionary(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        ultimo_cambio: datetime.datetime = datetime.datetime(2020, 5, 17)
        self.dictionary: dict = {
            "effort": [3, 4],
            "state": ["A", "D"],
            "last_change": [ultimo_cambio, ultimo_cambio],
        }
        self.dataframe: pd.DataFrame = pd.DataFrame.from_dict(self.dictionary)

    def test_row_dataframe_change_dictionary(self):
        """

        """
        diccionario = row_dataframe2dictionary(self.dataframe.iloc[0])
        self.assertEqual(diccionario["effort"], self.dictionary["effort"][0])
        self.assertEqual(diccionario["state"], self.dictionary["state"][0])
        self.assertEqual(diccionario["last_change"], self.dictionary["last_change"][0])
        diccionario = row_dataframe2dictionary(self.dataframe.iloc[1])
        self.assertEqual(diccionario["effort"], self.dictionary["effort"][1])


if __name__ == "__main__":
    unittest.main()
