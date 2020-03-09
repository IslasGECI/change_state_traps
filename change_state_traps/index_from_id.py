import pandas as pd

def make_dict_from_id_index(ids : str, index: int):
    dictionary : dict = {ids : index}
    return(dictionary)

def dictionary_for_initialization(initialization: pd.DataFrame):
    index_from_id = {}
    for index, row in initialization.iterrows():
        index_from_id.update({row['id']: index})
    return(index_from_id)