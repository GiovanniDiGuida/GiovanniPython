import xml.etree.ElementTree as ET

dati = [
{'nome': 'Alice', 'eta': '22'},
{'nome': 'Bob', 'eta': '25'},
{'nome': 'Charlie', 'eta': '20'}
]

root= ET.Element("studenti")


#Metodo normale
"""counter=1
for dato in dati:
    studente=ET.Element("studente", {"id":str(counter)})
    nome=ET.Element("nome")
    nome.text=dato["nome"]
    studente.append(nome)
    eta=ET.Element("eta")
    eta.text=dato["eta"]
    studente.append(eta)
    root.append(studente)
    counter+=1"""
#secondo metodo
counter=1
for dato in dati:
    studente=ET.Element("studente", {"id":str(counter)})
    for chiave,valore in dato.items():
        nome=ET.Element(chiave)
        nome.text=valore
        studente.append(nome)
        
    root.append(studente)
    counter+=1



tree= ET.ElementTree(root)
tree.write("file3.xml")