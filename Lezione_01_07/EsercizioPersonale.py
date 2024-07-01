
# Login
def login(utente,psw):
    cond= True
    x="admin"
    y=12345
    while cond:
        if utente==x and psw==y:
            cond= False
            print("Benvenuto, hai effettuato il login")
        else:
            print("Nome utente o password sbagliati")

#Presenza del file e visualizzazione prodotti    
import os

def visualizza_banco():
    if not os.path.exists("gestione.txt"):
        return
    else:
        with open ("gestione.txt","r") as file:
            banco = file.read()
            print(banco)

#Presenza del file e visualizzazione saldo
def visualizza_saldo():
    if not os.path.exists("gestione_contanti.txt"):
        return
    else:
        with open ("gestione_contanti.txt","r") as file:
            saldo = file.read()
            print(saldo)

#Gestione acquisto
def acquisto():
    lista=[]
    with open ("gestione.txt","r") as file:
            banco = file.read()
            print(banco)
            lista.append(banco)
            Acquisto=input("è stato fatt un acquisto? si/no ")
            if Acquisto== "si":
                print("ok")
                cosa=input("cosa è stato acquistato? ")
                if cosa in lista:
                    lista.remove(cosa)
                    with open ("gestione.txt","w") as file:
                        file.write(lista)
                        print(banco)
                    
                else:
                    print("L'elemento non è presente nel file")
            else:
                print("ok")

#Gestione contanti
def contanti():
    Acquisto=input("è stato fatt un acquisto? si/no ")
    if Acquisto== "si":
        print("ok")
    else:
        print("ok")
    
    with open ("gestione_contanti.txt","r") as file:
            saldo = file.read()
            print(saldo)
            x=int(input("Quanto è stato il valore?: "))
            saldo1= int(saldo)
            NuovoSaldo= saldo1-x
            with open ("gestione_contanti.txt","w") as file:
                file.write(NuovoSaldo)
                print(NuovoSaldo)


#Richiamo funzioni

print("Salve e benvenuto")
utente=input("Scrivi il nome utente: ")
psw=int(input("Scrivi la tua password: "))
login(utente,psw)

visualizza_banco()

visualizza_saldo()

acquisto()

contanti()
            

    
    
    


            


