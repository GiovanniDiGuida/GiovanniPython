class Animale:

    def __init__(self,nome,età):
        self.nome=nome
        self.età=età
    
    def fai_suono(self):
        print("Il suo suono è: ")

class Leone(Animale):

    def __init__(self,nome, età, tipo_animale):
        super().__init__(nome, età, tipo_animale)
        self.tipo_animale= tipo_animale
    
    def suono_(self):
        super().fai_suono()
        print("ruggito")
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, tipo: {self.tipo_animale}"

animale1= Leone("bob","10","leone")
print(animale1)
Leone.suono_()