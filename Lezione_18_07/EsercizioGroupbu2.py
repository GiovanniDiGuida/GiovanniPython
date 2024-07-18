import pandas as pd
import numpy as nd

"""citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
prodotti=['Tastiera', 'Mouse',"Monitor","Cuffie","Casse"]
data=['2021-01-01', '2021-02-01']
vendite=nd.random.randint(1,100,size=10)
costi=nd.random.randint(1,10,size=10)"""
class Prodotto:
    citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
    prodotti=['Tastiera', 'Mouse',"Monitor","Cuffie","Casse"]
    data=['2021-01-01', '2021-02-01']
    vendite=nd.random.randint(1,100,size=10)
    costi=nd.random.randint(1,10,size=10)

    def __init__(self):
        self.citta=Prodotto.citta
        self.prodotti=Prodotto.prodotti
        self.data=Prodotto.data
        self.vendite=Prodotto.vendite
        self.costi=Prodotto.vendite

    def crea(self):
        data = {
        'Data': nd.random.choice(self.data,size=10),
        'Città': nd.random.choice(self.citta,size=10),
        'Prodotto': nd.random.choice(self.prodotti,size=10),
        'Vendite': self.vendite}
         
        data2= {
            'Prodotto': nd.random.choice(self.prodotti,size=10),
            "Costi": self.costi}
        
        self.trasformato1=pd.DataFrame(data)
        self.trasformato2=pd.DataFrame(data2)
    
    def unisci(self):
        self.unito = pd.merge(self.trasformato1, self.trasformato2, on="Prodotto")
        print(self.unito)
    
    def pivot(self):
        pivot_unito = self.unito.pivot_table(values='Vendite', index='Città', columns='Prodotto', aggfunc='sum')
        print(pivot_unito)


negozio= Prodotto()
negozio.crea()
negozio.unisci()
negozio.pivot()
    