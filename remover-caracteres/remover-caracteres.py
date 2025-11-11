um = input("digite a primeria palavra, frase ou letras")
dois = input("digite a segunda palavra, frase ou letras")
tres = ""
ltres = []
for c in um:
    if not c in dois:
        tres += c
        ltres.append(c)
goin = "".join(ltres)
print(goin)
print(tres)
