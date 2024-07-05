class ContoBancario:
    def __init__(self, saldo_iniziale):
        self.__saldo = saldo_iniziale  # Attributo privato

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo} effettuato. Saldo attuale: {self.__saldo}")
        else:
            print("L'importo del deposito deve essere positivo.")

    

    def get_saldo(self):
        print(f"Saldo attuale: {self.__saldo}")

#Utilizzo della classe
conto = ContoBancario(1000)
conto.get_saldo()  #ci da la classe

conto.deposita(500)

