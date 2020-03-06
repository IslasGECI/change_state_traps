import unittest
from change_state_traps import *

class TestIndexFromId(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.Ids: list = ['id1']
        self.index: list = [2]

    def test_make_dict(self):
        """
        Verifica que la función `make_dict_from_id_index` genere el diccionario correcto. 
        """
        dictionary : dict = make_dict_from_id_index(self.index, self.id)
        self.assertEqual(dictionary[self.Ids[0]], self.index[0])

if __name__ == '__main__':
    unittest.main()