import numpy as np

"""Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti operazioni:
- calcolo della media;
- calcolo della deviazione standard;
- trasformarlo in un array 5x10"""

arr=np.random.randint(1,1000, size=50)

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

oggetto=Array(arr)
oggetto.mostra()
oggetto.media()
oggetto.deviazione()
oggetto.trasforma()

    