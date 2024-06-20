cond=True
while cond:
    x=input("Vuoi scrivere un numero? si/no")
    if x=="si":
        y=int(input("Scrivi Numero:"))
        if y % 2==0:
            print("Numero Pari")
        else:
            print("Numero Dispari")
    elif x=="no":
        cond=False
        print("Grazie per l'uso")
        
    else:
        ("Errore")

    