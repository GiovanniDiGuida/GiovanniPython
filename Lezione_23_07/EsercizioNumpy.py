import numpy as np

"""Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti operazioni:
- calcolo della media;
- calcolo della deviazione standard;
- trasformarlo in un array 5x10"""

arr=np.random.randint(1,1001, size=50)

class Array:

    def __init__(self,arr):

        self.arr=arr
    
    def mostra(self):
        print("L'array è: ")
        print(self.arr)
    
    def media(self):
        
        media=np.mean(self.arr)
        print("La media è: ")
        print(media)
    
    def deviazione(self):

        deviazione_st=np.std(self.arr)
        print("La deviazione standard è:")
        print(deviazione_st)
    
    def trasforma(self):
        arr.reshape(5,10)
        print("L'array trasformato è: ")
        print(arr)


print("Menù: ")
print("1)Crea e mostra array")
print("2)Mostra media")
print("3)Mostra deviazione standard")
print("4)Trasforma in un array 5x10")
print("5)Esci")

while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        oggetto=Array(arr)
        oggetto.mostra()
    elif scelta=="2":
        oggetto.media()
    elif scelta=="3":

        oggetto.deviazione()
    elif scelta=="4":
        oggetto.trasforma()
    elif scelta=="5":
        print("Grazie per l'uso")
        break

    