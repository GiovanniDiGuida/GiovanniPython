class Animale:

    def __init__(self,nome,età):
        self.nome=nome
        self.età=età
    
    def fai_suono(suono):
        print("Il suo suono è: "+suono)

class Leone(Animale):

    def __init__(self,nome, età, tipo_animale):
        super().__init__(nome, età)
        self.tipo_animale= tipo_animale
    
    def suono(self):
        Animale.fai_suono("ruggisce")

    
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, tipo: {self.tipo_animale}"

animale1= Leone("bob","10","leone")
print(animale1)
animale1.suono()
