cond= True
Lista=[]

while cond:
    Numero=input("Vuoi aggiungere un numero?: ")
    
    if Numero=="si":
        x=int(input("Aggiungi numero: "))
        if x>0:
            Lista.append(x)
        else:
            print("Numero negativo, non va bene")
    else:
        print("Grazie per l'uso")
        cond= False

print(Lista)
for i in Lista:
    i=(i)*"*"
    print(i)