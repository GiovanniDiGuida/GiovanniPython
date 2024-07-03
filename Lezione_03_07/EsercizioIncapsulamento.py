class ContoBancario:
    def __init__(self):
        self.__titolare="Giovanni"
        self.__saldo=30.50
    
    def deposita(self):
        while True:
            x=input("Vuoi depositare?: si/no")
            if x=="si":
                importo=float(input("Quanto vuoi depositare?: "))
                if importo>0:
                    nuovo_importo=self.__saldo + importo
                    self.__saldo=nuovo_importo
                elif importo<= 0:
                    print("Devi aggiungere denaro per depositare")
                else:
                    pass
            if x=="no":
                print("Grazie per l'uso")
                break
            else:
                pass
    
    def preleva(self):
        if self.__saldo > 0:
            while True:
                x=input("Vuoi prelevare?: si/no")
                if x=="si":
                    importo=float(input("Quanto vuoi prelevare?: "))
                    if importo>0:
                        nuovo_importo=self.__saldo - importo
                        self.__saldo=nuovo_importo
                    elif importo< 0:
                        print("Devi aggiungere un numero positivo per prelevare")
                    else:
                        pass
                if x=="no":
                    print("Grazie per l'uso")
                    break
                else:
                    pass
        
        elif self.__saldo <0:
            print("Non ci sono soldi da prelevare")
    
    def visualizza_saldo(self):
        self.__saldo=str(self.__saldo)
        print("Il tuo saldo è "+self.__saldo)
    
conto1= ContoBancario()
conto1.deposita()
conto1.preleva()
conto1.visualizza_saldo()

    

                