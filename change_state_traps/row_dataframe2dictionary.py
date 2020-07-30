import pandas as pd

def row_dataframe2dictionary(row_dataframe: pd.Series):
    dictionary: dict = row_dataframe.to_dict()
    return dictionary
