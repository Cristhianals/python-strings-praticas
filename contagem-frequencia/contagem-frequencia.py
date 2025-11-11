p = input("digite a primeria palavra, frase ou letras")
for l,b in enumerate(p):
    a = p.count(p[l])
    if not b in p[:l]: 
        print(f"{b} aparece {a} vezes no objeto")
