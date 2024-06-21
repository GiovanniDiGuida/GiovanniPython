cond= True

while cond:
    Numero=int(input("Inserisci numero intero positivo:"))
    if Numero > 0:
        for positivi in range(Numero+1):
            if positivi %2 ==0:
                print(positivi)


            #Ci stavo ragionando ma non ho fatto in tempo
