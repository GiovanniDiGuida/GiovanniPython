import pandas as pd
import numpy as np

class Negozio:
    def __init__(self):
        self.citta = ["Napoli", "Roma", "Torino", "Milano", "Genova", "Palermo", "Bologna", "Firenze", "Venezia", "Verona"]
        self.prodotti = ["Panna", "Pezzi Pane", "Acqua", "Passate", "Scatole lenticchie", "Scatole ceci", "Scatole fagioli"]
        self.quantità = np.random.randint(1, 30, size=10)
        self.prezzo = np.random.randint(1, 5, size=10)
    
    def crea(self):
        dati = {
            "Città": np.random.choice(self.citta, size=10),
            "Prodotti": np.random.choice(self.prodotti, size=10),
            "Prezzo": self.prezzo,
            "Quantità": self.quantità
        }
        self.negozio=pd.DataFrame(dati)
        print(self.negozio)
    
    def totale_vendite(self):
        prodotto_vendite=self.negozio["Prezzo"]*self.negozio["Quantità"]
        self.negozio["Totale Vendite"]= prodotto_vendite
        print(self.negozio)
    
    
    def raggruppa_per_prodotto(self):
        self.gruppo = self.negozio.groupby("Prodotti")["Quantità"].sum()
        print(self.gruppo)
    
    def più_venduto(self):
        venduto=self.gruppo.idxmax()
        print(venduto)
    
    def città(self):
        self.gruppo=self.negozio.groupby("Città")["Quantità"].sum().idxmax()
        print(self.gruppo)
    
    def vendite_superiori(self):
        venduto=pd.DataFrame(self.negozio)
        vendite_maggiori=venduto[venduto["Totale Vendite"] > 40]
        print(vendite_maggiori)
    
    def decrescente(self):
        negozio_ordinato = self.negozio.sort_values(by="Totale Vendite")
        negozio_ordinato_decrescente=negozio_ordinato[::-1]
        print(negozio_ordinato_decrescente)
    
    def ordinaPerCittà(self):
        ordinato=self.negozio.groupby("Città")["Quantità"].sum()
        print(ordinato)
    
"""class Prodotto(Negozio):
    def __init__(self):
        super().__init__()
        self.prodotti_vendite=self.negozio["Prezzo"]*self.negozio["Quantità"]
    
    def totale_vendite(self):
        self.negozio["Totale Vendite"]= self.prodotti_vendite
        print(self.negozio)
    
    def vendite_superiori(self):
        venduto=pd.DataFrame(self.negozio)
        vendite_maggiori=venduto[venduto["Totale Vendite"] > 40]
        print(vendite_maggiori)
    
    
    def decrescente(self):
        negozio_ordinato = self.negozio.sort_values(by="Totale Vendite")
        negozio_ordinato_decrescente=negozio_ordinato[::-1]
        print(negozio_ordinato_decrescente)"""


print("You shall not Pass")
print("Menù:")
print("1)Carica e visualizza dati")
print("2)Aggiungi e visualizza Vendite totali")
print("3)Visualizza il totale delle vendite per ciascun prodotto")
print("4)Visualizza il prodotto più venduto in termini di Quantità")
print("5)Identificare la città con il maggior volume di vendite totali")
print("6)Visualizza solo le vendite degli elementi superiori a 40")
print("7)Ordina per vendite totali in ordine decrescente")
print("8)Visualizza il numero di vendite per ogni città")
print("9)Esci")
negozio=None
gruppo=None
"""totale=None"""
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        negozio=Negozio()
        negozio.crea()
    elif scelta=="2":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            negozio.totale_vendite()
    elif scelta=="3":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            gruppo=negozio.raggruppa_per_prodotto()
    elif scelta=="4":
        if negozio is None or gruppo is None:
            print("devi creare il dizionario o aggiornare il dizionario con 'Totali Vendite'")
        else:
            gruppo.più_venduto()
    elif scelta=="5":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            negozio.città()
    elif scelta=="6":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            negozio.vendite_superiori()  
    elif scelta=="7":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            negozio.decrescente()
    elif scelta=="8":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            negozio.decrescente()
    elif scelta=="9":
        print("Grazie per l'uso")
        break
    else:
        print("Errore")
    

        
    
