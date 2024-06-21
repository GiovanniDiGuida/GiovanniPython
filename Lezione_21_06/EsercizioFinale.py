#Chiedere un numero positivo
Numero=int(input("Inserisci numero positivo:"))
while Numero <=0:
    Numero=int(input("Inserisci numero positivo:"))

#Genera lista di numeri
n=int(input("inserisci numero >1"))
for i in range(1,n+1):
    print (i)
#Somma numeri pari
sommapari=0
for z in range(2,i+1,2):
    sommapari+=z
    print(sommapari)
#Stampa numeri dispari
for c in range(1,i+1,2):
    print(c)



