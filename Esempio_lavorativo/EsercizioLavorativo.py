import pandas as pd
import numpy as nd

#Qui ci sono tutte le info per creare il dizionario(15min per farlo)
citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
nomi=["Giovanni","Andrea","Davide","Matteo","Lorenzo","Daniele","Amalia","Antonio","Valentina","Giacomo","Teresa","Danilo","Mirko","Tommaso","Salvatore"]
eta=nd.random.randint(18,80,size=30)
durata_abbonamento=nd.random.randint(1,12,size=30)
tariffa=[10,15,20,25]
dati_consumati_GB=nd.random.randint(1,5,size=30)
servizio_clienti=nd.random.randint(1,10,size=30)
churn=["Si","No"]

class Operatore:

    def __init__(self,citta,nomi,eta,durata_abbonamento,tariffa,dati_consumati_GB,servizio_clienti,churn):#Costruisco il costruttore(8 minuti)

        self.citta=citta
        self.nomi=nomi
        self.eta=eta
        self.abbonamento=durata_abbonamento
        self.tariffa=tariffa
        self.dati_consumati_GB=dati_consumati_GB
        self.servizio_clienti=servizio_clienti
        self.churn=churn
    
    def costruisci(self):#Creo il dizionario con i valore messi a self del costruttore(10 min)

        dati={"Città": nd.random.choice(self.citta,size=30),
              "Nomi": nd.random.choice(self.nomi,size=30),
              "Età": eta,
              "Abbonamento": durata_abbonamento,
              "Tariffa": nd.random.choice(self.tariffa,size=30),
              "GB_Usati": dati_consumati_GB,
              "Servizio_Clienti_usato":servizio_clienti,
              "Churn":nd.random.choice(self.churn,size=30)}
        
        self.trasformato=pd.DataFrame(dati)#Creo il dataframe del dizionario
        print(self.trasformato)
    
    def creafile(self):#Funzione che ci crea il file(3 min)
        self.trasformato.to_csv("Operatore.csv")
    
    def info(self):#2 min
        info1=self.trasformato.info()
        print(info1)
    
    def describe(self):#2 min
        describe1=self.trasformato.describe()
        print(describe1)
    
    def counts(self):#2min
        counts1=self.trasformato.value_counts()
        print(counts1)
    
    def
    

print("Menù:")
print("1)Carica e visualizza dati")
print("2)Crea un file CSV con questi dati")
print("3)Esamina la distribuzione dati")
print("4)")
print("5)")
print("6)")
print("7)")
print("8)")
print("9)Esci")


operatore=None
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore=Operatore(citta,nomi,eta,durata_abbonamento,tariffa,dati_consumati_GB,servizio_clienti,churn)
            operatore.costruisci()
    elif scelta=="2":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.creafile()
    elif scelta=="3":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            scelta2=input("Come vuoi esaminare i dati? info/describe/value_counts")
            if scelta2.lower()=="info":
                print("La distribuzione dati con info è: ")
                operatore.info
            elif scelta2.lower()=="describe":
                print("La distribuzione dati con describe è: ")
                operatore.describe()
            elif scelta2.lower()=="value_counts":
                print("La distribuzione dati con describe è: ")
                operatore.counts()
            else:
                print("Errore")
    elif scelta=="4":

            


        
#operatore=Operatore(citta,nomi,eta,durata_abbonamento,tariffa,dati_consumati_GB,servizio_clienti,churn)
#operatore.costruisci()
#operatore.creafile()
    

    

    


    

