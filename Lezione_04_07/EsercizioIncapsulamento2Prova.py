class Posto:
    

    def __init__(self,numero,fila):
        self.__numero=numero
        self.__fila=fila
        self.__occupato= False
    
    def prenota(self):
        posto=input("Vuoi prenotare?: si/no")
        if posto=="si":
            if self.__occupato==False:
                self.__occupato==True
        else:
            pass
    
    def libera(self):
        if self.__occupato== True:
            self.__occupato== False
    
    def get_fila(self):
        return print("La fila è: "+self.__fila)
    
    def get_numero(self):
        self.__numero=str(self.__numero)
        return print("Il numero è: "+self.__numero)
    
    def get_stato(self):
        if self.__occupato== False:
            print("Libero")
        else:
            print("Occupato")

class PostoVIP(Posto):
    def __init__(self, numero, fila,servizio_posto):
        super().__init__(numero, fila)

        self.__servizio_posto=servizio_posto
        self.__occupato1= False
    
    def servizio__posto(self):
        self.__occupato1=self.__occupato
        super().prenota()
        cibo=["patatine","popcorn","coca","fanta"]
        print(cibo)
        prenotazione=input("Cosa vuoi prenotare? :")
        if prenotazione.lower() in cibo:
            print("La tua richiesta verrà elaborata")
        else:
            print("Il prodotto non è presente nella lista")
    
    def libera(self):
        if self.__occupato1== True:
            self.__occupato1== False
    
    def get_fila(self):
        return print("La fila è: "+self.__fila)
    
    def get_numero(self):
        self.__numero=str(self.__numero)
        return print("Il numero è: "+self.__numero)
    
    def get_stato(self):
        if self.__occupato1== False:
            print("Libero")
        else:
            print("Occupato")
    
    

class PostoStandard(Posto):
    def __init__(self, numero, fila,tipo_prenotazione):
        super().__init__(numero, fila)

        self.__tipo_prenotazione=tipo_prenotazione
        self.__occupato2= False

    def prenotazione_online(self):
        tipo=input("Vuoi prenotare online?: si/no")
        if tipo=="si":
            prezzo=input("Il costo sarà maggioritario, vuoi procedere?: si/no ")
            if prezzo.lower()=="si":
                self.__occupato2== True
            else:
                pass
        elif tipo=="no":
            super().prenota()
            self.__occupato2= self.__occupato
        else:
            pass
    
    def libera(self):
        if self.__occupato2== True:
            self.__occupato2== False
    
    def get_fila(self):
        return print("La fila è: "+self.__fila)
    
    def get_numero(self):
        self.__numero=str(self.__numero)
        return print("Il numero è: "+self.__numero)
    
    def get_stato(self):
        if self.__occupato== False:
            print("Libero")
        else:
            print("Occupato")

class Teatro:
    
    def __init__(self):
        posti=[1,3,5,7,8]
        posti_occupati=[]

        self.__posti=posti
        self.__posti_occupati=posti_occupati
    
    def prenota_posto(self):
        print(self.__posti)
        posto=int(input("Che posto vuoi prenotare?"))
        if posto in self.__posti:
            self.__posti.remove(posto)
            self.__posti_occupati.append(posto)
    
    def get_posti_occupati(self):
        print("I posti prenotati sono: "+self.__posti_occupati)

        
    
        

print("Menù\n: 1)Posto\n 2)PostoVIP\n 3)PrenotazioneOnline\n 4)Teatro\n 5)Esci")
while True:
    fare=input("Cosa vuoi fare? :")
    if fare=="1":
        x=("Che posto vuoi visualizzare?: 1/2/3")
        if x=="1":
            posto1=Posto(1,"Fila 1")
            posto1.get_fila()
            posto1.get_numero()
            posto1.get_stato()
            y=input("Vuoi prenotare?")
            if y=="si":

                posto1.prenota()
                """posto1.libera()"""
            elif y=="no":
                pass
            else:
                print("Errore")
        elif x=="2":
            posto2=Posto(2,"Fila 1")
            posto2.get_fila()
            posto2.get_numero()
            posto2.get_stato()
            y=input("Vuoi prenotare?")
            if y=="si":

                posto2.prenota()
                """posto2.libera()"""
            elif y=="no":
                pass
            else:
                print("Errore")
        elif x=="3":
            posto3=Posto(3,"Fila 1")
            posto3.get_fila()
            posto3.get_numero()
            posto3.get_stato()
            y=input("Vuoi prenotare?")
            if y=="si":

                posto3.prenota()
                posto3.libera()
            elif y=="no":
                pass
            else:
                print("Errore")
    
    if fare=="2":
        postovip1=PostoVIP(4,"fila 2","Servizio al posto")
        postovip1.get_fila()
        postovip1.get_numero()
        postovip1.get_stato()
        x=input("Vuoi prenotare? si/no")
        if x=="si":
            postovip1.servizio__posto()
        else:
            pass
    

        





