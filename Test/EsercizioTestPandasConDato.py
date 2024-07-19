import pandas as pd
import numpy as nd

dati=pd.read_csv("TestNegozio.csv")

raggruppato = dati.groupby(["Data","Filiali"]).agg({"Vendite": "sum"})
print(raggruppato)
media= dati.groupby('Filiali')['Vendite'].mean()
print(media)
filiale_piùvendite= media.idxmax()
print(filiale_piùvendite)

dati["Media"]= media
dati["Filiale più Vendite"]=filiale_piùvendite

dati.to_csv("TestNegozioAggiornato.csv")

