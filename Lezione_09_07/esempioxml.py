import xml.etree.ElementTree as ET
"""
def xml_to_file():
    tree = ET.parse("path_to_file.xml")

    root = tree.getroot()

    return root"""

"""def xml_to_string():
xml_data = '''<?xml version="1.0"?>
<saluti>
<saluto>Hello World</saluto>
</saluti>'''

root = ET.fromstring(xml_data)

return root

#root = xml_to_file()

root = xml_to_string()

for saluto in root.findall('saluto'):
print(saluto.text)

#Funzione per avere dalla stringa all'albero
def xml_to_string():
xml_data = '''<?xml version="1.0"?>
<saluti>
<saluto id='1'>Hello World1</saluto>
<saluto id='2'>Hello World2</saluto>
<saluto id='3'>Hello World3</saluto>
</saluti>'''

root = ET.fromstring(xml_data)

tree = ET.ElementTree(root)

return tree, root

tree, root = xml_to_string()

tree.write("file2.xml")"""