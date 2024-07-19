import pandas as pd
import numpy as np

date=np.linspace(1, 30, 30)
vendite=np.random.randint(0,50,30)
ore=np.random.randint(4,9,30)

dati={"Date": date,
      "Vendite": vendite,
      "Ore":ore}

trasformato=pd.DataFrame(dati)
print(trasformato)

vendite_medie=trasformato["Vendite"]/trasformato["Ore"]
trasformato["Vendite Medie"]= vendite_medie
print(trasformato)

valoremassimo= trasformato.groupby("Date")["Vendite Medie"].max().idxmax()
valoreminimo= trasformato.groupby("Date")["Vendite Medie"].min().idxmin()
#valoremassimo2=valoremassimo.idxmax()
print("Il giorno del valore massimo è:")
print(valoremassimo)
print("Il giorno del valore minimo è: ")
print(valoreminimo)

