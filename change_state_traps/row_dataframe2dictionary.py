import pandas as pd
import datetime

def row_dataframe2dictionary(row_dataframe : pd.Series):
    ultimo_cambio : datetime.datetime = datetime.datetime(2020, 5, 17)
    dictionary : dict = {"effort" : 3, "state" : "A", "last_change" : ultimo_cambio}
    return(dictionary)