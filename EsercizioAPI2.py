"""Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in
caso non fosse presente vi permetterà di catturarlo salvando il numero
identificativo, nome, abilità, xp(punti esperienza),peso
e altezza.
(Sul sistema API sono presenti poco più di 1000 pokemon)"""

import requests
import json
import random
numero=random.randint(1,1300)
pokedex= requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}").text
dizionario_pokedex=json.loads(pokedex)
"""for i in dizionario_pokedex["results"]:
    print(dizionario_pokedex["results"]["nome"])"""
"""nome=dizionario_pokedex["results"][0][""]"""

"""print(nome)"""
print(dizionario_pokedex)