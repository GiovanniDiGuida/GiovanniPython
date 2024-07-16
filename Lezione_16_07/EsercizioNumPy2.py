import numpy as np

print("Ciao, benvenuto nel programma")
scelta1=input("Vuoi utilizzare il programma?: si/no ")
if scelta1=="si":
    x=int(input("Scegli il primo numero: "))
    y=int(input("Scegli il secondo numero: "))
    array=np.linspace(x,y,50)
else:
    print("Grazie")
#print(array)

array2=np.random.rand(50)
#print(array2)

array_uniti=array + array2
#print(array_uniti)
#print(np.sum(array_uniti))
#print(array_uniti[array_uniti >5])
#print(np.sum(array_uniti[array_uniti >5]))

print("Menù\n 1)Visualizza primo array\n 2)Visualizza secondo array\n 3)Visualizza array unito(somma singoli elementi)\n 4)Visualizza gli elementi >5 dell'array unito\n 5)Visualizza somma dell'array unito\n 6)Esci")
cond=True
while cond:
    scelta2=input("Cosa vuoi fare?: ")
    if scelta2=="1":
        print(array)
    elif scelta2=="2":
        print(array2)
    elif scelta2=="3":
        print(array_uniti)
    elif scelta2=="4":
        print(array_uniti[array_uniti >5])
    elif scelta2=="5":
        print(np.sum(array_uniti[array_uniti >5]))
    elif scelta2=="6":
        print("Grazie per l'uso")
        cond=False
    else:
        print("Errore")