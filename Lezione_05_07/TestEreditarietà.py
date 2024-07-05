
class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        pass   
    
    def mangia(self):
        print(f"{self.nome} sta mangiando.")
    
    


class Cane(Animale):

    def __init__(self, nome,tipo):
        super().__init__(nome)
        self.tipo=tipo

    def parla(self):
        print(f"{self.nome} dice: Bau!")
    
    def zampe(self):
        print(f"{self.nome} ha {self.tipo}")





cane = Cane("Chicca","Quattro zampe")


cane.parla()  
cane.mangia()
cane.zampe()  


