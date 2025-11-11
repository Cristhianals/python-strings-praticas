#jogodavelha = [
#    list("   |     |   "),
#    list("   |     |   "),
#    list("---+-----+---"),
#    list("   |     |   "),
#    list("   |     |   "),
#    list("---+-----+---"),
#    list("   |     |   "),
#    list("   |     |   ")
#]
#print("".join(x))
jogo = [
    list(" 7 | 8 | 9 "),
    list("---+---+---"), 
    list(" 4 | 5 | 6 "),
    list("---+---+---"),
    list(" 1 | 2 | 3 ")
]
ocupados = []
jogadores = ["X","O"]
print("")
cabo = False
while True:
    print("")
    for velha in jogo:
        print("".join(velha))
    if cabo:
        break
    if jogadores == []:
        jogadores = ["X","O"]
    posicao = int(input("\nEm qual posicao deseja colocar o {0:}(de 1 a 9): ".format(jogadores[0])))
    #if not posicao.isdigit():
        #print("\ndigite apenas numeros!")
        #continue
    if posicao <= 0 or posicao > 9:
        print("\nEssa posicao nao existe!")
        continue
    if posicao in ocupados:
        print("\nEssa posicao ja esta ocupada!")
        continue
    else:
        ocupados.append(posicao)
        if posicao == 1:
            jogo[4][1] = jogadores[0]
        elif posicao == 2:
            jogo[4][5] = jogadores[0]
        elif posicao == 3:
            jogo[4][9] = jogadores[0]
        elif posicao == 4:
            jogo[2][1] = jogadores[0]
        elif posicao == 5:
            jogo[2][5] = jogadores[0]
        elif posicao == 6:
            jogo[2][9] = jogadores[0]
        elif posicao == 7:
            jogo[0][1] = jogadores[0]
        elif posicao == 8:
            jogo[0][5] = jogadores[0]
        elif posicao == 9:
            jogo[0][9] = jogadores[0]
        jogadores.pop(0)
    if jogo[4][1] == jogo[0][9] and jogo[2][5] == jogo[0][9]:
        print("Jogador {:0} ganho".format(jogo[0][9]))
        jogo[1][7] = "/"
        jogo[3][3] = "/"
        cabo = True
    elif jogo[0][1] == jogo[4][9] and jogo[2][5] == jogo[4][9]:
        print("Jogador com {:0} ganho".format(jogo[4][9]))
        jogo[1][3] = "\\"
        jogo[3][7] = "\\"
        cabo = True
    elif jogo[4][1] == jogo[4][9] and jogo[4][5] == jogo[4][9]:
        print("Jogador {:0} ganho".format(jogo[4][9]))
        jogo[4][0] = "-"
        jogo[4][2] = "-"
        jogo[4][4] = "-"
        jogo[4][6] = "-"
        jogo[4][8] = "-"
        jogo[4][10] = "-"
        cabo = True
    elif jogo[2][1] == jogo[2][9] and jogo[2][5] == jogo[2][9]:
        print("Jogador {:0} ganho".format(jogo[2][9]))
        jogo[2][0] = "-"
        jogo[2][2] = "-"
        jogo[2][4] = "-"
        jogo[2][6] = "-"
        jogo[2][8] = "-"
        jogo[2][10] = "-"
        cabo = True
    elif jogo[0][1] == jogo[0][9] and jogo[0][5] == jogo[0][9]:
        print("Jogador com{:0} ganho".format(jogo[0][9]))
        jogo[0][0] = "-"
        jogo[0][2] = "-"
        jogo[0][4] = "-"
        jogo[0][6] = "-"
        jogo[0][8] = "-"
        jogo[0][10] = "-"
        cabo = True
    elif jogo[4][1] == jogo[0][1] and jogo[2][1] == jogo[0][1]:
        print("Jogador {:0} ganho".format(jogo[0][1]))
        jogo[1][1] = "|"
        jogo[3][1] = "|"
        cabo = True
    elif jogo[4][5] == jogo[0][5] and jogo[2][5] == jogo[0][5]:
        print("Jogador {:0} ganho".format(jogo[0][5]))
        jogo[1][5] = "|"
        jogo[3][5] = "|"
        cabo = True
    elif jogo[4][9] == jogo[0][9] and jogo[2][9] == jogo[0][9]:
        print("Jogador {:0} ganho".format(jogo[0][9]))
        jogo[1][9] = "|"
        jogo[3][9] = "|"
        cabo = True
    if len(ocupados) == 9:
        print("\nDeu velha!")
        cabo = True
