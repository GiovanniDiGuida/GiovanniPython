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
numero=random.randint(1,1002)
pokedex= requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}").text
dizionario_pokedex=json.loads(pokedex)
nome= dizionario_pokedex["forms"][0]["name"]
id=numero
abilità=[]
for dato in dizionario_pokedex["abilities"]:
    nome_abilità=dato["ability"]["name"]
    abilità.append(nome_abilità)

exp=dizionario_pokedex["base_experience"]
altezza=dizionario_pokedex["height"]
peso=float(dizionario_pokedex["weight"])
    


"""print(nome,id,abilità,exp,altezza,peso)"""

pokedex={}
id_pokemon=id
caratteristiche={"id":id,"nome":nome,"abilita":abilità,"exp":exp,"altezza":altezza,"peso":peso}
pokedex[id_pokemon]=[caratteristiche]
print(pokedex)
if pokedex=={}:
    json2= json.dumps(pokedex)

    
    with open("pokedex.json","w") as file:
        file.write(json2)
        print("file creato!")
else:
    json2= json.dumps(pokedex)

    
    with open("pokedex.json","a") as file:
        file.write(json2)
        print("pokemon aggiunto")