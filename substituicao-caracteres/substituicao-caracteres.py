um = input("digite a primeria palavra, frase ou letras")
dois = input("digite a segunda palavra, frase ou letras")
tres = input("digite a terceira palavra, frase ou letras")
quarta = []
quatro = ""
for i,a in enumerate(um):
    if a in dois:
        if i + 1 > len(dois):
            i = 0
        p = dois.find(a,i)
        if len(tres)-1 >= p:
            quarta.append(tres[p])
            quatro += tres[p]
        else:
            quarta.append(tres[-1])
            quatro += tres[-1]           
    else:
        quarta.append(a)
        quatro += a
j = "".join(quarta)
print(j)
print(quatro)
