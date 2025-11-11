um = input("digite a primeria palavra, frase ou letras")
dois = input("digite a segunda palavra, frase ou letras")
naotem = ""
naoacho = []
for a in um:
    if not a in dois:
        naotem += a
        naoacho.append(a)
for a in dois:
    if not a in um:
        naotem += a
        naoacho.append(a)
j = ""
print(j.join(naoacho))
print(j)
j = "".join(naoacho)
print(naotem)
naoteremos = ""
naoachamos = []
for a in um:
    index = dois.rfind(a)
    if index == -1:
        naoteremos += a
        naoachamos.append(a)

for a in dois:
    index = um.rfind(a)
    if index == -1:
        naoteremos += a
        naoachamos.append(a)
goin = "".join(naoachamos)
print(goin)
print(naoteremos)
