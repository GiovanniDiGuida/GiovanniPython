import numpy as np

array=np.random.randint(1,101,size=(6,6))
#print(array)
array4x4=array[1:5 , 1:5]
#print(array4x4)
array_invertito=array4x4[::-1]
#print(array_invertito)
array_invertito_diagonale= np.diagonal(array_invertito)
#print(array_invertito_diagonale)

#array_invertito[array_invertito % 3==0] = -1
#print(array_invertito)



print("Menù:\n 1)Visualizza Array\n 2)Visualizza array 4x4\n 3)Visualizza array invertito\n 4)Visualizza diagonale dell'array invertito\n 5)Sostituisci i multipli di 3 dell'array invertito con -1\n 6)Esci  ")
cond=True
while cond:
    scelta=input("Cosa vuoi fare?:")
    if scelta=="1":
        print(array)
    elif scelta=="2":
        print(array4x4)
    elif scelta=="3":
        print(array_invertito)
    elif scelta=="4":
        print(array_invertito_diagonale)
    elif scelta=="5":
        array_invertito[array_invertito % 3==0] = -1
        print(array_invertito)
    elif scelta=="6":
        print("Grazie per l'uso")
    else:
        print("Errore")


