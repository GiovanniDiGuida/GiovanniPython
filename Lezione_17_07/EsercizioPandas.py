import numpy as nd
import pandas as pd

def genera():
    nomi=["Giovanni","Andrea","Davide","Matteo","Lorenzo","Daniele","Amalia","Antonio","Valentina","Giacomo","Teresa","Danilo","Mirko","Tommaso","Salvatore"]
    citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
    eta=nd.random.randint(0,65,size=15)
    salario=nd.random.randint(15000,50000,size=15)
    dati={
        "Nome": nd.random.choice(nomi,size=15),
        "Città":nd.random.choice(citta,size=15),
        "Età":(eta),
        "Salario":(salario)
    }
    #print(dati)
    trasformato = pd.DataFrame(dati)
    print(trasformato)
    
    return trasformato

def estrai_prime_righe(trasformato):
    prime_righe=trasformato.head(5)
    
    print(prime_righe)

def estrai_ultime_righe(trasformato):
    ultime_righe=trasformato.tail(5)
    print(ultime_righe)

def tipo(trasformato):
    print(trasformato.info())

def media(trasformato):
    print("La media dell'età è: ")
    print(trasformato["Età"].mean())
    print("La media del salario è: ")
    print(trasformato["Salario"].mean())

def deviazione_standard(trasformato):
    print("La deviazione standard dell'età è: ")
    print(trasformato["Età"].var())
    print("La deviazione standard del salario è: ")
    print(trasformato["Salario"].var())

def mediana(trasformato):
    print("La mediana dell'età è: ")
    print(trasformato["Età"].median())
    print("La mediana del salario è: ")
    print(trasformato["Salario"].median())

def rimuovi_duplicati(trasformato):
    trasformato= trasformato.drop_duplicates("Nome")
    print(trasformato)

def sostituisci(trasformato):
    sostituto_età=trasformato["Età"].fillna(trasformato["Età"].median())
    print(sostituto_età)
    sostituto_salario=trasformato["Salario"].fillna(trasformato["Salario"].median())
    print(sostituto_salario)
    

def aggiungi(trasformato):

    trasformato['Giovane'] = trasformato['Età'] <= 18
    trasformato['Adulto'] = (trasformato['Età'] >= 19) & (trasformato['Età'] <= 65)
    trasformato['Senior'] = trasformato['Età'] >=66 
    print("Il dizionario aggiornato è: ")
    print(trasformato)
    return trasformato

def crea_file(trasformato):
    trasformato.to_csv('Stipendio.csv')

print("CIAOOOOOOOOOO")
print("Menù:")
print("1)Carica e visualizza dati")
print("2)Visualizza le prime 5 righe")
print("3)Visualizza le ultime 5 righe")
print("4)Visualizza media di età e salario")
print("5)Visualizza deviazione standard di età e salario")
print("6)Visualizza la mediana di età e salario")
print("7)Rimuovi i duplicati")
print("8)Sostituisci i valori vuoti con mediana")
print("9)Aggiungi categorie")
print("10)Visualizza le info")
print("11)Scrivi tutti in un file CSV")
print("12)Esci")
trasformato=None
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        trasformato=genera()
    elif scelta=="2":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            estrai_prime_righe(trasformato)
    elif scelta=="3":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            estrai_ultime_righe(trasformato)
    elif scelta=="4":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            media(trasformato)
    elif scelta=="5":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            deviazione_standard(trasformato)
    elif scelta=="6":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            mediana(trasformato)  
    elif scelta=="7":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            rimuovi_duplicati(trasformato)
    elif scelta=="8":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            sostituisci(trasformato)
    elif scelta=="9":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            aggiungi(trasformato)
    elif scelta=="10":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            tipo(trasformato)
    elif scelta=="11":
        if trasformato is None:
            print("devi creare il dizionario")
        else:
            crea_file(trasformato)
            print("Hai creato il file")
        break
    elif scelta=="12":
        print("Grazie per l'uso")
        break
    else:
        print("Errore")

