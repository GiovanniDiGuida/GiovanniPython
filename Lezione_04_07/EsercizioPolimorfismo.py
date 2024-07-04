class MetodoPagamento:
     
    def effettua_pagamento(self,importo):
        print("il costo è "+importo)
        x=input("Vuoi effettuare pagamento?: ")
        if x=="si":
            print("pagamento effettuato")
        else:
            pass

class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print("paghi con carta di credito")
        return super().effettua_pagamento(importo)

class PayPal(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print("Paghi con PayPal")
        return super().effettua_pagamento(importo)

class BonificoBancario(MetodoPagamento):

    def effettua_pagamento(self, importo):
        print("Paghi con bonifico bancario")
        return super().effettua_pagamento(importo)

class GestorePagamenti(MetodoPagamento):

    def _pagamento_(self,pagamento):
        return pagamento.effettua_pagamento(3)

pagamento1=MetodoPagamento
gestorepagamento= GestorePagamenti
gestorepagamento._pagamento_(pagamento1)