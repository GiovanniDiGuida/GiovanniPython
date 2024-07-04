class FabbricaCioccolato:

    def __init__(self,cacao,latte,zucchero):

        self.__ing1=cacao
        self.__ing2=latte
        self.__ing3=zucchero

class Pistacchio(FabbricaCioccolato):

    def __init__(self, cacao, latte, zucchero, pistacchio):
        super().__init__(cacao, latte, zucchero)

        self.__ing4=pistacchio
    
    def get_ing1(self):
        return print("L'ingrediente 1 è: "+self.__ing1)
    
    def get_ing2(self):
        return print("L'ingrediente 2 è: "+self.__ing2)
    
    def get_ing3(self):
        return print("L'ingrediente 3 è: "+self.__ing3)
    
    def get_ing4(self):
        return print("L'ingrediente 4 è: "+self.__ing4)

class Nocciole(FabbricaCioccolato):

    def __init__(self, cacao, latte, zucchero, nocciole):
        super().__init__(cacao, latte, zucchero)

        self.__ing5=nocciole
    
    def get_ing5(self):
        return print("L'ingrediente 5 è: "+self.__ing5)
    


