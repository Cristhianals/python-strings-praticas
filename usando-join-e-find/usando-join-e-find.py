um = input("digite a primeria palavra, frase ou letras")
dois = input("digite a segunda palavra, frase ou letras")
iguais = ""
igual = []
for a in um:
    if a in dois:
        iguais += a
        igual.append(a)
Join = "".join(igual)
print(Join)
print(iguais)
#usando find
achou = ""
achousse = []
for a in um:
    acho = dois.find(a)
    if acho > -1:
        achou += dois[acho]
        achousse.append(dois[acho])
j = "".join(achousse)
print(achou)
print(j)
