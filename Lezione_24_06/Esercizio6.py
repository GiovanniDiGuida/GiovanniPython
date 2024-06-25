""" Scrivete un programma che chiede un numero allutente e
restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{quadrato: 144,pari o dispari:pari, n. cifre: 2 }"""

Dizio={"Quadrato":"", "Pari/dispari":"", "N.cifre": "" }

x=int(input("Inserisci numero: "))
if x>0:
    Dizio["Quadrato"] = x*x
elif x%2== 0:
    Dizio["Pari/dispari"] = "pari"
elif x%2!= 0:
    Dizio["Pari/dispari"] = "dispari"
else:
    print("errore")

x=str(x)
Dizio["N.cifre"]= len(x)

print(Dizio)

