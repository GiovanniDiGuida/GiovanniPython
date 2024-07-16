import numpy as np


def crea():
    x=int(input("Scrivi numero righe: "))
    y=int(input("Scrivi numero colonne: "))
    array=np.random.randint(0,10,size=(x,y))
    print(array)
    return array,x,y

def estrazione(array,x,y):
    a=int(input("Inserisci inizio riga: "))
    b=int(input("Inserisci fine riga: "))
    c=int(input("Inserisci inizio colonna: "))
    d=int(input("Inserisci fine colonna: "))
    if a<x and b <x and c < y and d< y:
        sotto_matrice = array[a:b, c:d]
        print(sotto_matrice)
    else:
        print("La sottomatrice non può essere più grande della matrice")
    
    
def somma_matrice_principale(array):
    print(np.sum(array))

def moltiplicazione(array, x, y):
    array2 = np.random.randint(0, 10, size=(x, y))
    array_moltiplicazione = array * array2
    print(array2)
    print("Matrice moltiplicazione:")
    print(array_moltiplicazione)

def media(array):
    print(np.mean(array))

def determinante(array,x,y):
    if x==y:
        determinante = np.linalg.det(array)
        print(determinante)

print("Ciao e benvenuto =) ")
print("Menù\n 1)Crea e visualizza array\n 2)Visualizza una sottomatrice\n 3)Somma della matrice principale\n 4)Moltiplica con un'altra matrice\n 5)Fai la media della matrice originale\n 6)Visualizza il determinante\n 7)Esci")
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        array,x,y=crea()
    elif scelta=="2":
        estrazione(array,x,y)
    elif scelta=="3":
        somma_matrice_principale(array)
    elif scelta=="4":
        moltiplicazione(array,x,y)
    elif scelta=="5":
        media(array)
    elif scelta=="6":
        determinante(array,x,y)     
    elif scelta=="7": 
        print("Grazie per l'uso")
        break 
    else:
        print("Errore")

