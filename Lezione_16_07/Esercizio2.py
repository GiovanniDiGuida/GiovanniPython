import numpy as np

array=np.arange(1, 26)
#print(array)

array5x5=array.reshape(5,5)
#print(array5x5)

#print(array5x5[2])
#print(array[10:15])

diagonale=np.diagonal(array5x5)
#print(diagonale)

#print(np.sum(diagonale))


print("Menù\n 1)Visualizza array\n 2)Trasforma array 5x5\n 3)Visualizza terza riga della matrice\n 4)Visualizza diagonale della matrice\n 5)Visualizza somma della diagonale\n 6)Esci")
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        print(array)
    elif scelta=="2":
        
        print(array5x5)
    elif scelta=="3":
        print(array5x5[2])
        print(array[10:15]) #secondo metodo
    elif scelta=="4":
        print(diagonale)
    elif scelta=="5":
        print(np.sum(diagonale))
    elif scelta=="6":
        print("Grazie per l'uso")
        break
    else:
        print("Errore")