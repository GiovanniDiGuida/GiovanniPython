import pandas as pd
import numpy as nd


#Qui ci sono tutte le info per creare il dizionario(15min per farlo)
citta=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
nomi=["Giovanni","Andrea","Davide","Matteo","Lorenzo","Daniele","Amalia","Antonio","Valentina","Giacomo","Teresa","Danilo","Mirko","Tommaso","Salvatore"]
eta=nd.random.randint(18,80,size=30)
durata_abbonamento=nd.random.randint(1,12,size=30)
tariffa=[10,15,20,25,50,100]
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
    
    def costruisci(self):#Creo il dizionario con i valore messi a self del costruttore(10 min)["Età","Durata_Abbonamento","GB_Usati","Servizio_Clienti_usato"]

        dati={"Città": nd.random.choice(self.citta,size=30),
              "Nomi": nd.random.choice(self.nomi,size=30),
              "Età": eta,
              "Durata_Abbonamento": durata_abbonamento,
              "Tariffa": nd.random.choice(self.tariffa,size=30),
              "GB_Usati": dati_consumati_GB,
              "Servizio_Clienti_usato":servizio_clienti,
              "Churn":nd.random.choice(self.churn,size=30)}
        
        self.trasformato=pd.DataFrame(dati)#Creo il dataframe del dizionario
        print(self.trasformato)
    
    def creafile(self):#Funzione che ci crea il file(3 min)
        print("File creato con successo")
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
    
    def pulisci_righe(self):#7 min (non ricordavo la funzione)
        eliminato=self.trasformato.dropna()
        print(eliminato)
    
    def pulisci_valori(self):#15 min non capivo cosa fare
        pulito=self.trasformato.fillna("Vuoto")
        print(pulito)
    
    def errori(self):
        tariffa_corretta=[5,10,15,20]
        self.trasformato[self.trasformato["Tariffa"] > 25]= nd.random.choice(tariffa_corretta)
        print(self.trasformato)
    
    def costo_per_GB(self):#5 min
        costo= self.trasformato["Tariffa"]/self.trasformato["GB_Usati"]
        self.trasformato["Costo_per_GB"]= costo
        print(self.trasformato)
    
    def groupEtà(self):#2min
        relazione_età=self.trasformato.groupby("Età").sum()
        print(relazione_età)
    
    def groupAbbonamento(self):#1min
        relazione_durataabbonamento=self.trasformato.groupby("Durata_Abbonamento").sum()
        print(relazione_durataabbonamento)
    
    def groupTariffa(self):#1min
        relazione_tariffa=self.trasformato.groupby("Tariffa").sum()
        print(relazione_tariffa)
    
    def groupChurn(self):#1min
        relazione_churn=self.trasformato.groupby("Churn").sum()
        print(relazione_churn)
    
    def correlazione(self):#15 min per capire un minimo cosa sia la correlazione
        correlazione=self.trasformato[['Età', 'Durata_Abbonamento', 'Tariffa', 'GB_Usati', 'Servizio_Clienti_usato']].corr()
        print("La correlazione è :")
        print(correlazione)
    
    def correlazione_ken(self):#15 min per capire un minimo cosa sia la correlazione
        correlazione=self.trasformato[['Età', 'Durata_Abbonamento', 'Tariffa', 'GB_Usati', 'Servizio_Clienti_usato']].corr(method= "kendall")
        print("La correlazione col metodo kendal è :")
        print(correlazione)
    
    def correlazione_spearman(self):#15 min per capire un minimo cosa sia la correlazione
        correlazione=self.trasformato[['Età', 'Durata_Abbonamento', 'Tariffa', 'GB_Usati', 'Servizio_Clienti_usato']].corr(method= "spearman", min_periods = 2)
        print("La correlazione col metodo Spearman è :")
        print(correlazione)
    
    def sostituisci_Churn(self):#10 minuti per cercare il metodo
        self.trasformato['Churn'] = self.trasformato['Churn'].map({'No': 0, 'Si': 1})
        print("La conversione è :")
        print(self.trasformato)
    
    def normalizzare(self):#30 minuti per cercare di capire
        lista=["Età","Durata_Abbonamento","GB_Usati","Servizio_Clienti_usato"]
        for elemento in lista:
            valore_minimo=self.trasformato[elemento].min()
            valore_massimo=self.trasformato[elemento].max()
            self.trasformato[elemento]=(self.trasformato[elemento]- valore_minimo)/(valore_massimo-valore_minimo)
        print(self.trasformato)

        

    
    

    
#1 ora per fare il menù e i dovuti controlli
print("Menù:")
print("1)Carica e visualizza dati")
print("2)Crea un file CSV con questi dati")
print("3)Esamina la distribuzione dati")
print("4)Elimina righe con valori nulli")
print("5)Elimina i singoli valori nulli")
print("6)Visualizza il costo per GB")
print("7)Visualizza la relazione tra Età, Durata_Abonnamento, Tariffa e la Churn")
print("8)Elimina errori di Tariffa")
print("9)Mostra la correlazione tra gli elementi")
print("10)Mostra la correlazione con metodo Kendal")
print("11)Mostra la correlazione con metodo Spearman")
print("12)Convertire la colonna Churn in formato numerico")
print("13)Normalizza")
print("14)Esci")


operatore=None
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
    
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
                operatore.info()
            elif scelta2.lower()=="describe":
                print("La distribuzione dati con describe è: ")
                operatore.describe()
            elif scelta2.lower()=="value_counts":
                print("La distribuzione dati con describe è: ")
                operatore.counts()
            else:
                print("Errore")
    elif scelta=="4":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.pulisci_righe()
    elif scelta=="5":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.pulisci_valori()
    elif scelta=="6":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.costo_per_GB()
    elif scelta=="7":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            print("Scegli quale relazione: 1)Con Età\n 2)Con Durata Abbonamento\n 3)Con Tariffa\n 4)Con Churn\n 5)Vedi tutte le relazioni ")
            scelta3=input("Quale relazione vuoi visualizzare?")
            if scelta3=="1":
                print("La relazione con Età è: ")
                operatore.groupEtà()
            elif scelta3=="2":
                print("La relazione con Durata abbonamento è: ")
                operatore.groupAbbonamento()
            elif scelta3=="3":
                print("La relazione con Tariffa è: ")
                operatore.groupTariffa()
            elif scelta3=="4":
                print("La relazione con Churn è: ")
                operatore.groupChurn()
            elif scelta3=="5":
                print("La relazione con Età è: ")
                operatore.groupEtà()
                print("La relazione con Durata abbonamento è: ")
                operatore.groupAbbonamento()
                print("La relazione con Tariffa è: ")
                operatore.groupTariffa()
                print("La relazione con Tariffa è: ")
                operatore.groupTariffa()
            else:
                print("Errore")
    elif scelta=="8":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.errori()
    elif scelta=="9":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.correlazione()
    elif scelta=="10":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.correlazione_ken()
    elif scelta=="11":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.correlazione_spearman()
    elif scelta=="12":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.sostituisci_Churn()
    elif scelta=="13":
        if operatore is None:
            print("Devi creare prima il file")
        else:
            operatore.normalizzare()
    elif scelta=="14":
        print("Grazie per l'uso")
        break
    else:
        ("Errore")
        

        
    

    

    


    
