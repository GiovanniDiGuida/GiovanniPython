class Ristorante:

    stato= False
    menù={}
    piatti_ordinati=[]

    
    def stato_apertura2(self):
        x=input("Il ristorante è aperto? si/no")
        if x=="si":
            self.stato= True
            print("Ristorante aperto: Benvenuto")
        elif x=="no":
            print("Il ristorante è chiuso")
            pass
        else:
            pass

    def __init__(self,nome,tipo_cucina):

        self.nome=nome
        self.tipo_cucina=tipo_cucina
    
    def menù_(self):
        while True:
            y=input("Vuoi aggiungere piatti? si/no")
            if y=="si":
                z=input("Come si chiama il piatto?: ")
                c=int(input("Quanto costa?:"))
                self.menù[z]= c
            elif y=="no":
                break
            else:
                print("Errore digitalizzazione")
    
    def rimuovi_piatti(self):
        x=input("Quale piatto vuoi rimuovere?: ")
        if x.lower() in self.menù:
            self.menù.pop(x)
        else:
            print("Il piatto non è presente nel menù")
        
        print(self.menù)
                

    def stamp_menù(self):
        print(self.menù)
    
    def ordinazione_(self):
        x=input("Cosa ha ordinato il cliente?: ")
        self.piatti_ordinati.append(x.lower())
        
    
    
    
    
    def __str__(self):
        return f"nome: {self.nome}, Tipo cucina: {self.tipo_cucina}"
    
class Ordinazione:
    piatti_ordinati=[]

    def ordinazione_cliente(self):
        print(Ristorante.stamp_menù)
        cliente=("Cosa vuoi ordinare? ")
        if cliente in Ristorante.stamp_menù:
            self.piatti_ordinati.append(cliente.lower())


    
    

ristorante1= Ristorante("Zia Bella","Casareccia")
print(ristorante1)
ristorante1.stato_apertura2()
ristorante1.menù_()
ristorante1.stamp_menù()
ristorante1.rimuovi_piatti()
ordinazione=input("Il cliente ha ordinato qualcosa? si/no: ")
if ordinazione=="si":
    
elif ordinazione=="no":
    print("va bene")
else:
    ("Errore digitalizzazione")



        