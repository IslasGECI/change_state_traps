import pandas as pd
import datetime

def row_dataframe2dictionary(row_dataframe : pd.Series):
    dictionary : dict = row_dataframe.to_dict()
    return(dictionary)