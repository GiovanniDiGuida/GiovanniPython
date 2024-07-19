import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

temperature=np.random.randint(20,30,size=30)

dati={"Temperature":temperature}

trasformato=pd.DataFrame(dati)
print(trasformato)

media=trasformato["Temperature"].mean()
print(media)
massimo=trasformato["Temperature"].max()
print(massimo)
minimo=trasformato["Temperature"].min()
print(minimo)
mediana = trasformato["Temperature"].median()
print(mediana)

categorie=["Media", "Massimo", "Minimo", "Mediana"]
valori=[media,massimo,minimo,mediana]
colori=["blue","red","yellow","green"]

plt.figure()
plt.bar(categorie, valori, color=colori)
plt.title("Dati temperatura")
plt.xlabel("Tipo di dato")
plt.ylabel('Valori')
plt.show()


