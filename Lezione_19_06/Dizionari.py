cane = {"nome": "Chicca",
        "età": 2,
        "sesso":"Femmina"}
cane["città"] = "Mugnano di Napoli"
print(cane)

gatto= {"nome": "Rengar",
        "età": 5,
        "sesso": "maschio"}
gatto["città"] = "Mugnano di Napoli"
print(gatto)
print(cane.keys())
print(gatto.keys())
print(cane.get("nome"))
print(gatto.get("sesso"))