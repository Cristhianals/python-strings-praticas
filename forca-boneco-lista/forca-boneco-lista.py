#palavra = input("Digite a palavra  secreta:").lower().strip()
boneco = [
list("X==:=="),
list("X  :  "),
list("X     "),
list("X     "),
list("X     "),
list("X===========")
]
palavras = ["abracadabra","banana","escada","salsicha","abacate","limao","ferrugem","sal","chiclete"]
numero = int(input("digite um numero:"))
palavra = palavras[(numero * 776) % len(palavras)]
for x in range(40):
    print()
digitados = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "-"
    print(senha)
    if senha == palavra:
        print("voce acertou!")
        break
    tentativa = input("\ndigite uma letra:").lower().strip()
    if tentativa in digitados:
        print("voce ja tententou essa letra!")
        continue
    else:
        digitados += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("voce errou!")
        #boneco = [
            #list("X==:=="),
            #list("X  :  "),
            #list("X     "),
            #list("X     "),
            #list("X     "),
            #list("X===========")
        #]
        if erros >= 1:
            boneco[2][3]= "0"
        if erros == 2:
            boneco[3] = list("X  |  ")
        elif erros == 3:
            boneco[3][2] = "/"
        if erros >= 4:
            boneco[3][4] = "\\"
        if erros == 5:
            boneco[4][2] = "/"
        elif erros >= 6:
            boneco[4][4] = "\\"
        for x in boneco:
            print("".join(x))
        if erros == 6:
            print("enforcado")
            print("a palavra era \n{:0}".format(palavra))
            break
