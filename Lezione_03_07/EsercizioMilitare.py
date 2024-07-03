class UnitàMilitare:
    def __init__(self,nome_unità,numero_soldati):

        self.nome_unità=nome_unità
        self.numero_soldati=numero_soldati
    
    def muovi(self):
        cosa_fa=input("Che movimento deve fare?")
        print("L'unità va a: "+cosa_fa)
    
    def attacco(self):
        attacco=input("L'unità deve attaccare?: si/no ")
        if attacco=="si":
            print("l'unità deve attaccare")
        elif attacco=="no":
            print("L'unità non deve attaccare")
    
    def ritira(self):
        ritiro=input("L'unità deve ritirarsi?: si/no ")
        if ritiro=="si":
            print("L'unità si ritira")
        else:
            pass

class Fanteria(UnitàMilitare):

    def __init__(self, nome_unità, numero_soldati,tipo):
        super().__init__(nome_unità, numero_soldati)

        self.tipo=tipo
    
    def costruisci_trince(self):
        trincee_costruite=0
        x=int(input("indica il numero di difese temporanee costruite: "))
        for i in range(x):
            if i >0:
                trincee_costruite+=1

        print("Il numero di difese è: "+trincee_costruite)

class Artigliera(UnitàMilitare):

    def __init__(self, nome_unità, numero_soldati, tipo):
        super().__init__(nome_unità, numero_soldati)
        
        self.tipo=tipo
    
    def calibra_artiglieria(self):
        artiglieria={}
        while True:
            pezzi=input("Vuoi aggiungere pezzi?: ")
            if pezzi=="si":
        
                y=input("Che tipo di artiglieria? ")
                x=input(int("Quanti pezzi ci sono?"))
                if x>0:
                    artiglieria[y]= x
                    
                elif x<0:
                    print("Devi aggiungere un numero positivo")
                elif x==0:
                    print("Non ci sono munizioni per: "+y)
                    artiglieria[y]= x
                else:
                    print("Devi scrivere un numero")
            if pezzi=="no":
                break
            else:
                print("Errore digitalizzazione")
        
        print(artiglieria)
        
                    

        """print("Il numero di pezzi è: "+x)"""

class Cavalleria(UnitàMilitare):

    def __init__(self, nome_unità, numero_soldati, tipo):
        super().__init__(nome_unità, numero_soldati)
        
        self.tipo=tipo
    
    def esplora_terreno(self):
        zone=["nord","sud","est","ovest"]
        zone_esplorate={}
        while True:
            cond=input("Si devono esplorare zone?:")
            if cond.lower()=="si":
                x=input("Quale zona deve esplorare?: ")
                if x in zone:
                    km=int(input("Scrivi i da esplorare: "))
                if km>0:
                    esplorata=input("la zona è stata esplorata?: si/no")
                    if esplorata=="si":
                        zone_esplorate[x]= km
                    elif esplorata=="no":
                        print("La zona non è stata esplorata")
                    else:
                        pass
                else:
                    pass
            elif cond.lower()=="no":
                break
            else:
                print("errore")
                

        print("La zone esplorate sono: "+zone_esplorate)
    
class SupportoLogistico(UnitàMilitare):
    def __init__(self, nome_unità, numero_soldati, tipo):
        super().__init__(nome_unità, numero_soldati)
        
        self.tipo=tipo
    
    def rifornisci_unità(self):
        mezzi={}
        rifornimento={}

        x=input("quale unità è stata fatta manutenzione?: ")
        if x !="":
            quanti=int(input("quanti?: "))
            mezzi[x]=quanti
        
        y=int(input("quante unità sono stato rifornite?: "))
        if y>0:
            unità=input("quali unità?: ")
            rifornimento[unità]= y
        elif y==0:
            print("Nessuna unità è stata rifornita")
        else:
            print("errore")
        
        print("i mezzi revisionati sono: "+mezzi)
        print("Le unità rifornite sono: "+rifornimento)
    """def visualizza(self):
        print(f"mezzi: {self.mezzi}")"""

        
class Ricognizione(UnitàMilitare):
    def __init__(self, nome_unità, numero_soldati, tipo):
        super().__init__(nome_unità, numero_soldati)
        
        self.tipo=tipo
    
    def conduci_ricognizione(self):
        missioni=[]

        x=int(input("quante missioni di sorveglianza sono state effettuate?: "))
        missioni.append(x)
        print(missioni)

"""class ControlloMilitare"""

unità1=Fanteria("Aquila","1000","Fanteria")
unità1.costruisci_trince