class Veicolo:

    def __init__(self,marca,modello,anno):
        self.__marca=marca
        self.__modello=modello
        self.__anno=anno
        self.__accensione= False
    
    def accendi(self):
        if self.__accensione== False:
            self.__accensione== True
    
    def spegni(self):
        if self.__accensione== True:
            self.__accensione== False

class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)

        self.__numero_porte= numero_porte
    
    def accendi(self):
        if self.__accensione== False:
            self.__accensione== True
    
    def spegni(self):
        if self.__accensione== True:
            self.__accensione== False
    
    def suona_clacson(self):
        return "Stai suonando il clacson(non esagerare)"
    
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
        return self.__modello

class Furgone(Veicolo):

    def __init__(self, marca, modello, anno, capacità):
        super().__init__(marca, modello, anno)

        self.__capacità=capacità
    
    def carica(self):
        return
    
    def scarica(self):
        return
    
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
        return self.__modello
    
    def get_capacità(self):
        return self.__capacità

class Motocicletta(Veicolo):

    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)


        self.__tipo=tipo
    
    def esegui_wheelie(self):
        if self.__tipo=="sportiva":
            print("Esegue wheelie")
    
class GestoreParcoVeicoli(Auto,Furgone,Motocicletta):

    def __init__(self):
        veicoli=[]

        self.__veicoli=veicoli
    
    def aggiungi_veicolo(self,veicolo):
        self.__veicoli.append(veicolo)
    
    def rimuovi_veicolo(self):
        marca=input("scrivi marca: ")
        modello=input("scrivi modello: ")

        for i in self.__veicoli:
            if marca==self.__marca and modello==self.__modello:
                self.__veicoli.remove(i)
            else:
                pass
    
    def lista_veicoli(self):
        return ("La lista è"+self.__veicoli)

veicolo1= Auto("Fiat","Panda","2010","4 porte")
veicolo2= Auto("Fiat","500","2005","4 porte")        
veicolo3= Auto("Fiat","Musa","2010","4 porte") 

parcoauto=GestoreParcoVeicoli
parcoauto.aggiungi_veicolo(veicolo1)
parcoauto.aggiungi_veicolo(veicolo2)
parcoauto.aggiungi_veicolo(veicolo3)
parcoauto.lista_veicoli()

        
        


    
    
    

        

