import numpy as np

def crea():
    array=np.random.randint(10,50,size=(4,4))
    print(array)
    return array
def indici(array):
    indice1=[0,1]
    print (array[indice1])
    indice2=[1,3]
    print (array[indice2])
    indice3=[2,2]
    print (array[indice3])
    indice4=[3,0]
    print (array[indice4])

def dispari(array):
    array_dispari=array[1::2]
    print(array_dispari)

def aggiungi(array):
    valore=int(input("Aggiungi un numero: "))
    array_nuovo=array+valore
    print(array_nuovo)


print("Menù\n 1)Crea e visualizza array\n 2)Visualizza indici(0, 1),(1, 3),(2, 2) e (3, 0)\n 3)Visualizza valori dispari\n 4)Aggiungi valore\n 5)Esci")
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        array=crea()
    elif scelta=="2":
        indici(array)
    elif scelta=="3":
        dispari(array)
    elif scelta=="4":
        aggiungi(array)
    elif scelta=="5":
        print("Grazie per l'uso")
        break
        
    else:
        print("Errore")


