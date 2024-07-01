class Ristorante:

    stato= False
    menù={}

    def stato_apertura1(self):
        if self.stato:
            print("Ristorante chiuso")
    def stato_apertura2(self):
        x=input("Il ristorante è aperto? si/no")
        if x=="si":
            self.stato= True
            print("Ristorante aperto")
        else:
            print("Il ristorante è chiuso")

    def __init__(self,nome,tipo_cucina):

        self.nome=nome
        self.tipo_cucina=tipo_cucina
    
    def menù_(self):
        y=input("Vuoi aggiungere piatti? si/no")
        if y=="si":
            z=input("Come si chiama il piatto?")
            c=int(input("Quanto costa?:"))
            self.menù[z]= c
    
    
    
    def stamp_menù(self):
        print(self.menù)
        
    
    
    
    
    def __str__(self):
        return f"nome: {self.nome}, : {self.tipo_cucina}"
    

ristorante1= Ristorante("Zia Bella","Casareccia")
print(ristorante1)
ristorante1.stato_apertura1()
ristorante1.stato_apertura2()
ristorante1.menù_()
ristorante1.stamp_menù()



        