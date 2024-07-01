class Biblioteca:

    def __init__(self):

        autore=input("scegli nome")
        titolo=input("Scegli titolo")
        pagine=input("inserisci pagine")

    

        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine
    
    def __str__(self):
        return f"titolo: {self.titolo}, Autore: {self.autore}, pagine: {self.pagine}"
    
"""libro1= Biblioteca()
print(libro1)"""

lista=[]
cond= True
while cond:
    x=input("Vuoi aggiungere libro? si/no")
    if x=="si":
        Biblioteca()
        lista.append(Biblioteca)
    else:
        print("Grazie per l'uso")
        cond= False

print(lista)

