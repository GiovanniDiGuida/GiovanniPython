"""Scrivete un programma che chiede una stringa all utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2} """

stringa = input("Inserisci una stringa:")

frequenza_comparsa={} 
for carattere in stringa:
    occorrenza = stringa.count(carattere)
    frequenza_comparsa[carattere] = occorrenza
