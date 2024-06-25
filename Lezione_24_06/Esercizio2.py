print("\n Menù")
print("Somma +")
print("Sottrazione -")
print("Moltiplicazione *")
print("Divisione /")
z=input("Cosa vuoi fare?: ")
if z=="+":
    x=int(input("inserisci numero 1"))
    y=int(input("inserisci numero 2"))
    c=x+y
    print("La somma dei due numeri è" +str(c))
elif z=="-":
    x=int(input("inserisci numero 1"))
    y=int(input("inserisci numero 2"))
    c=x-y
    print("La sottrazione dei due numeri è" +str(c))
elif z=="*":
    x=int(input("inserisci numero 1"))
    y=int(input("inserisci numero 2"))
    c=x*y
    print("La moltiplicazione dei due numeri è" +str(c))
elif z=="/":
    x=int(input("inserisci numero 1"))
    y=int(input("inserisci numero 2"))
    c=x/y
    print("La divisione dei due numeri è" +str(c))
else:
    print("Errore")

    
