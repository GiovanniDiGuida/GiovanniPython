class Personale_Cucina:

    def __init__(self,nome,età):

        self.nome=nome
        self.età=età

    def lavora(metodo):

        print("La sua mansione è: "+ metodo)

class Chef(Personale_Cucina):

    def __init__(self, nome, età,specialità):
        super().__init__(nome, età)

        self.specialità= specialità
    
    def prepara_menu(self):
        piatti= []
        while True:
            aggiungi=input("Vuoi aggiungere piatto? si/no: ")
            if aggiungi=="si":
                nuovo_piatto=input("nome piatto: ")
                piatti.append(nuovo_piatto)
            elif aggiungi=="no":
                break
            else:
                print("Errore")
        
        print(piatti)
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, specialità: {self.specialità}"

class SousChef(Personale_Cucina):
    
    def __init__(self, nome, età,specialità):
        super().__init__(nome, età)

        self.specialità=specialità
    
    def inventario(self):
        inventario=["piatti","olio","patate"]
        while True:
            modifica=input("Vuoi modificare inventario? si/no: ")
            if modifica=="si":
                cosa=input("Cosa vuoi rimuovere?: ")
                if cosa in inventario:
                    inventario.remove(cosa)
                else:
                    print("l'elemento non è presente nell'inventario")
            elif modifica=="no":
                break
            else:
                print("Errore")
        
        print(inventario)
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, specialità: {self.specialità}"
    
    

class Cuoco_linea(Personale_Cucina):

    def __init__(self, nome, età, specialità):
        super().__init__(nome, età)
        self.specialità=specialità
    
    def cucina_piatto(self):
        print("e specializzato nella preparazione di carne e pesce")
        
        
        
        
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, specialità: {self.specialità}"


chef= Chef("Giovanni","30","Giapponese")
print(chef)
Personale_Cucina.lavora("comandare")
chef.prepara_menu()

chef1=SousChef("Paolo","35","Messicana")
print(chef1)
Personale_Cucina.lavora("Aiutare lo chef")
chef1.inventario()

chef2=Cuoco_linea("Marco","40","Greca")
print(chef2)
Personale_Cucina.lavora("Organizzare")
chef2.cucina_piatto()
