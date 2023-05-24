import change_state_traps
import datetime
import pandas as pd

ultimo_cambio = datetime.datetime(2000, 5, 17)
argumentos = {"effort": 0, "capture": 0, "state": "D", "last_change": ultimo_cambio}
transecto = []
cambio_estado = pd.read_csv("cambio_estado.csv")
ID = cambio_estado["ID"].unique()
id_and_index = {}
for trampa in range(len(ID)):
    id_and_index.update({ID[trampa]: trampa})
    transecto.append(Trap(**argumentos))