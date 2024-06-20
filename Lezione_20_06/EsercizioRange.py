cond= True
Numero=int(input("InserisciNumero:"))
for i in range(Numero,-1,-1):
    print (i) 

Condizione=input("Vuoi aggiungere un altro numero? (si/no)")

while cond:
 if Condizione== "si":
   Numero=int(input("InserisciNumero:"))
 for i in range(Numero,-1,-1):
    print (i) 
 elif Condizione=="no":
 cond= False
 print("Grazie per l'utilizzo")
else:
    ("Errore")


