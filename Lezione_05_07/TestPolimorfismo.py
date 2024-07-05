#Classe base
class Animale:
    def parla(self):
        return print("L'animale fa: ")

#Classe derivata 
class Cane(Animale):
    def parla(self): #Sovrascrive
        return "wof"

#Classe derivata 
class Gatto(Animale): #Sovrascrive
    def parla(self):
        return "Miao!"


def fai_parlare_animale(animale):
    print(animale.parla())

#Polimorfismo
animale1=Cane()
animale2=Gatto()

fai_parlare_animale(animale1)
fai_parlare_animale(animale2)