controllo_ciclo1= True
# Variabili
Tavolo={"Tavolo1": "legno",
           "prezzo": 500,
           "quantità":3}
Sedia={"Sedia1": "legno",
       "prezzo": 200,
       "quantità": 10}
Tovaglia={"tovaglia1": "cotone",
          "prezzo": 10,
          "quantità":50}
Tavolo=="tavolo"
Sedia=="sedia"
Tovaglia=="tovaglia"
Inventario=["tavolo","sedia","tovaglia"]
InventarioAcquisti=[]
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
            InventarioAcquisti.insert("tavolo")
            print(InventarioAcquisti)
        if compra=="sedia":
            InventarioAcquisti.insert("sedia")
            print(InventarioAcquisti)
        if compra=="tovaglia":
            InventarioAcquisti.insert("tovaglia")
            print(InventarioAcquisti)
            
    elif Selezione==3:
        print("Buona giornata, Grazie")
    else:
        print("Errore Selezione")
    
        