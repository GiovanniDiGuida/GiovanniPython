"""Scrivere un programma Python che modifica un documento 
XML esistente.Considera il seguente documento XML:
<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>
Il programma dovrebbe aggiungere un nuovo libro al documento XML 
e stampare il documento risultante."""

import xml.etree.ElementTree as ET

dati="""<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>"""

root= ET.fromstring(dati)

libro_nuovo=ET.Element("libro")

titolo=ET.Element("titolo")
inserisci=input("Inserisci titolo: ")
titolo.text=inserisci
libro_nuovo.append(titolo)
autore=ET.Element("autore")
inserisci1=input("Inserisci autore: ")
autore.text=inserisci1
libro_nuovo.append(autore)
root.append(libro_nuovo)

tree= ET.ElementTree(root)
tree.write("libro_nuovo.xml")

