nome=input("Inserisci nome:")
anno=int(input("Inserisci anno di nascita:"))
eta=(2024-anno)
x=int(input("Inserisci giorno settimana a numero:"))
y= 6-x

print("il tuo nome è " + nome + ", hai " + str(eta) + " e mancano " +str(y)+ " giorni a Sabato")