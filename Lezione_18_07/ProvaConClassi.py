import pandas as pd
import numpy as nd


class Prodotto:
    """citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
    prodotti=['Tastiera', 'Mouse',"Monitor","Cuffie","Casse"]
    data=['2021-01-01', '2021-02-01']
    vendite=nd.random.randint(1,100,size=10)"""
    
    def __init__(self):
        citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
        prodotti=['Tastiera', 'Mouse',"Monitor","Cuffie","Casse"]
        data=['2021-01-01', '2021-02-01']
        vendite=nd.random.randint(1,100,size=10)
        self.citta=citta
        self.prodotti=prodotti
        self.data=data
        self.vendite=vendite
    
    def crea(self):
        data = {
    'Data': nd.random.choice(self.data,size=10),
    'Città': nd.random.choice(self.citta,size=10),
    'Prodotto': nd.random.choice(self.prodotti,size=10),
    'Vendite': self.vendite}
        self.trasformato = pd.DataFrame(data)
        print(self.trasformato)
    
    def pivot(self):
        pivot_trasformato = self.trasformato.pivot_table(values='Vendite', index='Città', columns='Prodotto', aggfunc='mean')
        print(pivot_trasformato)
    
    def grup(self):
        gruppo=self.trasformato.groupby("Prodotto").sum()
        print(gruppo)

negozi=Prodotto()
negozi.crea()
negozi.pivot()
negozi.grup()