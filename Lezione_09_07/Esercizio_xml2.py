"""Scrivere un programma Python che crea un documento XML basatosu dati
 forniti. Ad esempio, considera il seguente elenco di studenti:
studenti = [
{'nome': 'Alice', 'eta': '22'},
{'nome': 'Bob', 'eta': '25'},
{'nome': 'Charlie', 'eta': '20'}
]
Il programma dovrebbe creare un documento XML che rappresenti questi studenti.
Infine esportatelo come file."""

import xml.etree.ElementTree as ET

dati = [
{'nome': 'Alice', 'eta': '22'},
{'nome': 'Bob', 'eta': '25'},
{'nome': 'Charlie', 'eta': '20'}
]

root= ET.Element("studenti")

#tree= ET.ElementTree(root)

for dato in dati:
    studente= ET.SubElement(root,"studente")
    nome= ET.SubElement(studente,"nome",{"Bob","Alice"})
    età= ET.SubElement(studente,"eta",{"22","25"})


tree= ET.ElementTree(root)
tree.write("file3.xml")



