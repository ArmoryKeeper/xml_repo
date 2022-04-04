import xml.etree.ElementTree as tree

root = tree.Element("Filmovi")



m1 = tree.Element("Film")
root.append(m1)
imeFilma = tree.SubElement(m1,"Ime")
imeFilma.text = "Sam u kuci"
zanrFilma = tree.SubElement(m1,"Zanr")
zanrFilma.text="Komedija"
godinaIzdanja = tree.SubElement(m1,"Godina_izdanja")
godinaIzdanja.text="1999"



m2 = tree.Element("Film")
root.append(m2)
imeFilma = tree.SubElement(m2,"Ime")
imeFilma.text = "Interstellar"
zanrFilma = tree.SubElement(m2,"Zanr")
zanrFilma.text="Sci-fi"
godinaIzdanja = tree.SubElement(m2,"Godina_izdanja")
godinaIzdanja.text="2015"

treee = tree.ElementTree(root)

#Ispis XML-a u vidu stringa
print(tree.tostring(root))

#Test gde pravimo XML fajl kako bismo proverili strukturu
with open("filmovi.xml","wb") as f:
    treee.write(f)


