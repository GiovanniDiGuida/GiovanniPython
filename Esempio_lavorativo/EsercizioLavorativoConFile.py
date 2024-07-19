import pandas as pd
import numpy as nd



file=pd.read_csv("Operatore.csv")
class Operatore:

    def __init__(self,file):#Costruisco il costruttore(8 minuti)

        self.trasformato=file

        
    
    def costruisci(self):

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
        #città_giuste=["Napoli","Roma","Torino","Milano","Genova","Palermo","Bologna","Firenze","Venezia","Verona"]
        tariffa_corretta=[5,10,15,20]
        self.trasformato[self.trasformato["Tariffa"] > 25]= nd.random.choice(tariffa_corretta)
        self.trasformato[self.trasformato["Età"]< 10]= nd.random.randint(18,80)
        #if self.trasformato["Città"] is not  città_giuste:
            #self.trasformato[self.trasformato["Città"]]= nd.random.choice(città_giuste)
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
    
    def correlazione_pearson(self):#15 min per capire un minimo cosa sia la correlazione
        
        correlazione=self.trasformato[['Età', 'Durata_Abbonamento', 'Tariffa', 'GB_Usati', 'Servizio_Clienti_usato']].corr(method= "pearson",numeric_only = True)
        print("La correlazione col metodo pearson è :")
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
print("8)Elimina errori di Tariffa e Età")
print("9)Mostra la correlazione tra gli elementi")
print("10)Mostra la correlazione con metodo Pearson")
print("11)Mostra la correlazione con metodo Spearman")
print("12)Convertire la colonna Churn in formato numerico")
print("13)Normalizza")
print("14)Esci")


operatore=None
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
    
        operatore=Operatore(file)
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
            operatore.correlazione_pearson()
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
        

        
    

    

    


    