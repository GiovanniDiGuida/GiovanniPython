import numpy as np

array = np.arange(10, 50)
#print(array)

tipo_dato=array.dtype

#print(tipo_dato)
def nuovo_tipo():
    tipo_nuovo=np.array(array,dtype='float64')
    print(tipo_nuovo.dtype)
#print(array.shape)


cond=True
print("Menù:\n 1)Visualizza Array 2)Visualizza tipo di dato 3)Cambiare il tipo di dato e visualizzarlo 4)Visualizzare forma array 5)Esci ")

while cond:
    cosa=input("Cosa vuoi fare?")
    if cosa=="1":
        print(array)
    elif cosa=="2":
        print(tipo_dato)
    elif cosa=="3":
        nuovo_tipo()
    elif cosa=="4":
        print(array.shape)
    elif cosa=="5":
        print("Grazie per l'uso")
        cond=False
    else:
        ("Errore")


