def casuale(z):
    x=40
    cond= True
    while cond:
        n=int(input("inserisci un numero"))
        if n<x:
            print("il numero è più piccolo")
        elif n>x:
            print("il numero è più grande")
        elif n==x:
            print("Bravo hai indovinato")
            cond= False

n=int(input("inserisci un numero"))
casuale("ciao")

        
        
    
