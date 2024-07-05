"""Create un gestionale bancario basato sulla programmazione a oggetti, 
la prima parte dell'esercizio riguarda solamente aggiunta e 
eliminazione cliente con il suo conto bancario e modifica cliente"""

class Cliente:
    def __init__(self, nome, età,carta_credito,cvc):

        self.__nome=nome
        self.__età=età
        self.__carta_credito=carta_credito
        self.__cvc=cvc

    def get_nome(self): 
        return self.__nome
    
    def get_cvc(self):
        return self.__cvc
    
    def set_nome(self, nome):
        self.__nome = nome

class GestioneBanca(Cliente):
    def __init__(self):
        self.__clienti = []
    
    def aggiungi_cliente(self,cliente):
        self.__clienti.append(cliente)
    
    def rimuovi_cliente(self, nome, cvc):
        for cliente in self.__clienti:
            if nome == cliente.get_nome() and cvc == cliente.get_cvc():
                self.__clienti.remove(cliente)
                print("Cliente rimosso.")
            else:
                print("Cliente non registrato")



    
banca=GestioneBanca()

while True:
    menu()
    scelta=input("Inserisci la scelta: ")
    if scelta=="1":
        while True:
            nome=input("Inserisci il nome del nuovo cliente: ")
            if nome.isalpha():
                break
            else:
                print("Inserisci solo lettere")
        while True:
            try:
                eta=int(input("Inserisci l'età del cliente: "))
                break
            except:
                print("ERRORE")
        while True:
            try:
                carta_credito=int(input("Inserisci il numero della carta di credito: "))
                break
            except:
                print("ERRORE")
        while True:
            cvc=input("Inserisci il cvc della carta: ")
            if len(cvc)!=3:
                print("cvc non conforme")
            else:
                break
        nuovo_cliente=Cliente(nome, eta,carta_credito,cvc)
        banca=banca.aggiungi_cliente(nuovo_cliente)
    elif scelta=="2":
        pass
    elif scelta=="3":
        pass
    elif scelta=="0":
        break