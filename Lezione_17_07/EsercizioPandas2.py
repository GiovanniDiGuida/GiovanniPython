import pandas as pd 
import numpy as nd


def crea():
    citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
    prodotti=["Panna","Pezzi Pane","Acqua","Passate","Scatole lenticchie","Scatole ceci","Scatole fagioli"]
    quantità=nd.random.randint(1,30,size=10)
    prezzo=nd.random.randint(1,5,size=10)

    dati={"Città": nd.random.choice(citta,size=10),
          "Prodotti": nd.random.choice(prodotti,size=10),
          "Prezzo": (prezzo),
          "Quantità": (quantità)}
    
    negozio=pd.DataFrame(dati)
    print(negozio)
    return negozio
    
def totale_vendite(negozio):
    prodotto_vendite=negozio["Prezzo"]*negozio["Quantità"]
    negozio["Totale Vendite"]= prodotto_vendite
    print(negozio)
    return negozio

def raggruppo(negozio):
    gruppo=negozio.groupby("Prodotti")["Quantità"].sum()
    print(gruppo)
    return gruppo

def più_venduto(gruppo):
    venduto=gruppo.idxmax()
    print(venduto)

def città(negozio):
    gruppo=negozio.groupby("Città")["Quantità"].sum().idxmax()
    print(gruppo)

def vendite_superiori(negozio):
    venduto=pd.DataFrame(negozio)
    vendite_maggiori=venduto[venduto["Totale Vendite"] > 40]
    print(vendite_maggiori)

def decrescente(negozio):
    negozio_ordinato = negozio.sort_values(by="Totale Vendite")
    negozio_ordinato_decrescente=negozio_ordinato[::-1]
    print(negozio_ordinato_decrescente)


def ordinaPerCittà(negozio):
    ordinato=negozio.groupby("Città")["Quantità"].sum()
    print(ordinato)


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
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        negozio=crea()
    elif scelta=="2":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            totale_vendite(negozio)
    elif scelta=="3":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            gruppo=raggruppo(negozio)
    elif scelta=="4":
        if negozio is None or gruppo is None:
            print("devi creare il dizionario o aggiornare il dizionario con 'Totali Vendite'")
        else:
            più_venduto(gruppo)
    elif scelta=="5":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            città(negozio)
    elif scelta=="6":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            vendite_superiori(negozio)  
    elif scelta=="7":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            decrescente(negozio)
    elif scelta=="8":
        if negozio is None:
            print("devi creare il dizionario")
        else:
            ordinaPerCittà(negozio)
    elif scelta=="9":
        print("Grazie per l'uso")
        break
    else:
        print("Errore")
    

#negozio=crea()
#totale_vendite(negozio)
#gruppo=raggruppo(negozio)
#più_venduto(gruppo)
#città(negozio)
#vendite_superiori(negozio)
#decrescente(negozio)
#ordinaPerCittà(negozio)


