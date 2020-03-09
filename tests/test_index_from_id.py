import unittest
from change_state_traps import *

class TestIndexFromId(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.Ids: list = ['id1', 'id2']
        self.index: list = [2, 4]
        self.effort: list = [25, 36]
        self.state: list = ["A", "D"]
        self.dictionary: dict = {'id2': 4, 'id1': 2}
        self.data_frame : pd.DataFrame = pd.DataFrame({'id': self.Ids,
        'effort': self.effort,
        'state': self.state})

    def test_make_dict(self):
        """
        Verifica que la función `make_dict_from_id_index` genere el diccionario correcto. 
        """
        dictionary : dict = make_dict_from_id_index(self.Ids[0], self.index[0])
        self.assertEqual(dictionary[self.Ids[0]], self.index[0])
        dictionary : dict = make_dict_from_id_index(self.Ids[1], self.index[1])
        self.assertEqual(dictionary[self.Ids[1]], self.index[1])

    def test_dictionary_for_initialization(self):
        """
        Verifica que se generan los diccionarios para inicializar el cambiador
        """
        ids_and_index = dictionary_for_initialization(self.data_frame)
        self.assertEqual(ids_and_index[self.Ids[1]], self.index[1])

if __name__ == '__main__':
    unittest.main()