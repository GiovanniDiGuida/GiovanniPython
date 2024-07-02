class Prodotto:
    
    nome1=input("scrivi nome: ")
    costo_produzione=int(input("Scrivi prezzo produzione: "))
    prezzo_vendita=int(input("Scrivi prezzo vendita: "))

    def __init__(self):

        self.nome=self.nome1
        self.costo_prod=self.costo_produzione
        self.prezzo_vend=self.prezzo_vendita
    
    """def __str__(self):
        return f"nome: {self.nome}, costo produzione: {self.costo_prod}, e il prezzo di vendita è: {self.prezzo_vend}"""

    def calcola_profitto(self):
        differenza=self.prezzo_vendita - self.costo_produzione
        print(differenza)
        
    x=input("Di cosa fa parte?: ")
    if x.lower()=="elettronica":
        class Elettronica:

            garanzia=int(input("Scrivi anni garanzia"))


            def __init__(self):

                self.gar=self.garanzia
            
            def __str__(self):
                return f"nome: {Prodotto.nome}, costo produzione: {Prodotto.costo_prod}, e il prezzo di vendita è: {Prodotto.prezzo_vend}, la differenza è: {Prodotto.calcola_profitto()}, e la garanzia è {self.gar}"

    elif x.lower()=="abbigliamento":
        class Abbigliamento:

            qualità=input("Scrivi la qualità")

            def __init__(self):

                self.qual=self.qualità

            def __str__(self):
                return f"nome: {Prodotto.nome}, costo produzione: {Prodotto.costo_prod}, e il prezzo di vendita è: {Prodotto.prezzo_vend}, la differenza è: {Prodotto.calcola_profitto()}, e la garanzia è {self.qualità}"
            

        """class Magazzino:

            inventario={}

            def __init__(self):
                
                self.inventario[Prodotto.nome]= Prodotto.calcola_profitto()
                print(self.inventario)
            """
            


prodotto1=Prodotto()
print(prodotto1)

"""elettronica1=Elettronica()
print(elettronica1)
abbigliamento1=Abbigliamento()
print(abbigliamento1)"""