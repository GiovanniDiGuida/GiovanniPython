"""Tre attributi: titolo, autore e pagine.

Un metodo descrizione che restituisca una stringa del tipo
"Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine."."""

class Libro:
    
    def __init__(self,titolo,autore,pagine):

        self.titolo= titolo
        self.autore= autore
        self.pagine= pagine

    def __str__(self):
        return f"titolo: {self.titolo}, Autore: {self.autore}, pagine: {self.pagine}"
    
    

    
libro1= Libro("Che bello phyton","Antonio","100")
libro2= Libro("Che bello phyton2","Giovanni","100")
libro3= Libro("Che bello phyton3","Marco","100")

print(libro1)
print(libro2)
print(libro3)