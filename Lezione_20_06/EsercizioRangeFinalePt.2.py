x=int(input("inserisci un numero più piccolo:"))
y=int(input("inserisci un numero più grande:"))
z=input("Vuoi numeri primi o pari? 1/2")
if z=="1":
    for primi in range(x,y+1):
        if primi %2 !=0:
            print(primi)
elif z=="2":
    for non_primi in range(x,y+1):
        if non_primi %2 !=0:
            print(non_primi)
else:
     print("Errore")


