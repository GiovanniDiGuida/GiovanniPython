class FabbricaCioccolato:#classe padre

    def __init__(self,cacao,latte,zucchero):# costruttore

        self.__ing1=cacao
        self.__ing2=latte
        self.__ing3=zucchero

class GestioneInventario: #classe gestione inventario
    def init(self):
        self.dizionario_ingredienti = self.riempi_dizionario_ingredienti()#costruttore 

    def riempi_dizionario_ingredienti(self):#riempire il dizionario
        ingredienti = ["zucchero", "cacao", "latte"]#partiamo da una lista
        dizionario_ingredienti = {}

        for ingrediente in ingredienti:#aggiunta ingredienti
            quantita = input(f"Inserisci la quantità di {ingrediente}: ")#inserisci quantità dell'ingrediente
            dizionario_ingredienti[ingrediente] = quantita#aggiunta ingredienti nel dizionario

        return dizionario_ingredienti

    def mostra_ingredienti(self):#mostrare l'inventario
        for ingrediente, quantita in self.dizionario_ingredienti.items():
            print(f"{ingrediente}: {quantita}")

class Pistacchio(FabbricaCioccolato,GestioneInventario):#classe figlia

    def __init__(self, cacao, latte, zucchero, pistacchio):#costruttore
        super().__init__(cacao, latte, zucchero)

        self.__ing4=pistacchio
    
    def get_ing1(self):#per prendere i valori privati
        return print("L'ingrediente 1 è: "+self.__ing1)
    
    def get_ing2(self):#per prendere i valori privati
        return print("L'ingrediente 2 è: "+self.__ing2)
    
    def get_ing3(self):#per prendere i valori privati
        return print("L'ingrediente 3 è: "+self.__ing3)
    
    def get_ing4(self):#per prendere i valori privati
        return print("L'ingrediente 4 è: "+self.__ing4)
    
    def aggiungi_ingredienti(self):#prova aggiunta ingrediente nuovo
        print(self.dizionario_ingredienti)
        x=int(input("Indica quantità pistacchio"))
        self.dizionario_ingredienti["pistacchio"]=x
        

class Nocciole(FabbricaCioccolato,GestioneInventario):

    def __init__(self, cacao, latte, zucchero, nocciole):
        super().__init__(cacao, latte, zucchero)

        self.__ing5=nocciole
    
    def get_ing5(self):
        return print("L'ingrediente 5 è: "+self.__ing5)
    
    def aggiungi_ingredienti(self):
        print(self.dizionario_ingredienti)
        x=int(input("Indica quantità nocciola"))
        self.dizionario_ingredienti["nocciola"]=x
    


class GestioneInventario:
    def init(self):
        self.dizionario_ingredienti = self.riempi_dizionario_ingredienti()

    def riempi_dizionario_ingredienti(self):
        ingredienti = ["zucchero", "cacao", "latte"]
        dizionario_ingredienti = {}

        for ingrediente in ingredienti:
            quantita = input(f"Inserisci la quantità di {ingrediente}: ")
            dizionario_ingredienti[ingrediente] = quantita

        return dizionario_ingredienti

    def mostra_ingredienti(self):
        for ingrediente, quantita in self.dizionario_ingredienti.items():
            print(f"{ingrediente}: {quantita}")

class Ricette:

    def ricetta_cioccolato_latte():
        print("Ricetta per cioccolato al latte:")
        print("- 100g di zucchero")
        print("- 50g di cacao")
        print("- 200ml di latte")
    
    def ricetta_cioccolato_nocciola():
        print("Ricetta per cioccolato al nocciola:")
        print("- 100g di zucchero")
        print("- 50g di cacao")
        print("- 200ml di latte")
        print("- 50gr nocciole")
    
    def ricetta_cioccolato_pistacchio():
        print("Ricetta per cioccolato al nocciola:")
        print("- 100g di zucchero")
        print("- 50g di cacao")
        print("- 200ml di latte")
        print("- 50gr pistaccchio")
    

class Produzione(GestioneInventario):
    def cioccolato_latte(self, inventario):
        barrette_cioccolato_l = 0

        while True:
            if inventario.dizionario_ingredienti.get("zucchero", 0) >= 100 and \
               inventario.dizionario_ingredienti.get("cacao", 0) >= 50 and \
               inventario.dizionario_ingredienti.get("latte", 0) >= 200:
                barrette_cioccolato_l += 1
                inventario.dizionario_ingredienti["zucchero"] -= 100
                inventario.dizionario_ingredienti["cacao"] -= 50
                inventario.dizionario_ingredienti["latte"] -= 200
                print(f"Prodotta una barretta di cioccolato al latte. Totale barrette: {barrette_cioccolato_l}")
            elif barrette_cioccolato_l >= 50:
                print("Raggiunto il massimo di 50 barrette di cioccolato al latte.")
                break
            else:
                print("Ingredienti insufficienti per la produzione di cioccolato al latte.")
                break

        return barrette_cioccolato_l

    
    


"""Esempio di utilizzo:
gestione_inventario = GestioneInventario()
gestione_inventario.mostra_ingredienti()

Ricette.ricetta_cioccolato_latte()

Produzione.cioccolato_latte(gestione_inventario)"""

"""print("Menù:\n 1)CioccolatoLatte\n 2)CioccolatoNocciola\n 3)CioccolatoPistacchio\n 4)VediIngredienti\n 5)Esci")
while True:
    x=input("Cosa vuoi fare: ")
    if x=="1":

    elif x=="2":

    elif x=="3":

    elif x=="4":

    elif x=="5":
        print("Grazie per l'uso")
        break
    else:
        print("Errore digitalizzazione")"""