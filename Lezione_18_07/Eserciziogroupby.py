import pandas as pd
import numpy as nd
citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
prodotti=['Tastiera', 'Mouse',"Monitor","Cuffie","Casse"]
data=['2021-01-01', '2021-02-01']
vendite=nd.random.randint(1,100,size=10)
data = {
    'Data': nd.random.choice(data,size=10),
    'Città': nd.random.choice(citta,size=10),
    'Prodotto': nd.random.choice(prodotti,size=10),
    'Vendite': vendite
}


trasformato = pd.DataFrame(data)
print(trasformato)

pivot_trasformato = trasformato.pivot_table(values='Vendite', index='Città', columns='Prodotto', aggfunc='mean')
print(pivot_trasformato)


gruppo=trasformato.groupby("Prodotto").sum()
print(gruppo)