um = input("digite a primeria palavra, frase ou letras")
dois = input("digite a segunda palavra, frase ou letras")
existe = um.find(dois)
if existe > -1:
    print(f"encontramos ({dois}, o segundo objeto) no primerio objeto digitado")
    print(f"ele esta localiazado na {existe + 1}º posicao")
    print(f"o primerio obejto é {um}")
    print(f"apartir da posicao {existe + 1}º, temos {um[existe:]}")
else:
    print(f"nao ha ({dois}) em nenhum lugar em ({um})")
