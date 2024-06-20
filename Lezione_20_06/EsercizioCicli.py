controllo_ciclo1= True
# Variabili
Inventario=["tavolo","sedia","tovaglia"]
# Gestione Clienti
print("\nMenu:")
print("1: Visualizza Inventario")
print("2: Acquista prodotto")
print("3: Esci")
Selezione=input("\n Cosa vuoi fare?")
while True:
#Visualizzare Inventario
    if Selezione==1:
       print(Inventario)
    #Acquisto oggetti
    elif Selezione==2:
        print(Inventario)
        compra=input("scegli oggetto:")
        if compra=="tavolo":
            Inventario.remove("tavolo")
            print(Inventario)
        if compra=="sedia":
            Inventario.remove("sedia")
            print(Inventario)
        if compra=="tovaglia":
            Inventario.remove("tovaglia")
            print(Inventario)
    elif Selezione==3:
        print("Buona giornata, Grazie")
    else:
        print("Errore Selezione")
    
        