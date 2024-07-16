import numpy as np

x=int(input("inserisci un numero: "))
y=int(input("inserisci un numero: "))
array= np.random.randint(x,y,20) #creazione array
#print(array)

#print(array[0:11])

#print(array[-5:])

#print(array[5:15])

#print(array[::3])

def cambia_numeri(): #sostituzione
    indice2=[5,6,7,8,9,10]
    array[indice2]=99
    print(array)

cond=True
print("Menù:\n 1)Visualizza Array\n 2)Visualizza i primi 10 elementi\n 3)Visualizza gli ultimi 5 elementi\n 4)Visualizzare gli elementi da 5 a 15(escluso)\n 5)Visualizza sempre il terzo elemento\n 6)Modifica elemento da 5 a 10\n 7)Esci  ")
while cond:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        print(array) #visualizza array
    elif scelta=="2":
       print(array[0:11]) #visualizza i primi 10 elementi
    elif scelta=="3":
        print(array[-5:]) #visualizza gli ultimi 5 elementi
    elif scelta=="4":
        print(array[5:15]) #visualizza gli elementi da 5 a 15
    elif scelta=="5":
        print(array[::3]) # step di 3
    elif scelta=="6":
        cambia_numeri() #sostituzione
    elif scelta=="7":
        print("Grazie per l'uso")
        cond=False
    else:
        print("Errore")



