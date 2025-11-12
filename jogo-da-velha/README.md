# Jogo da Velha - Dois Jogadores

## 📋 Enunciado

Escreva um jogo da velha para dois jogadores. O jogo deve:

- Perguntar a posição onde cada jogador quer jogar.
- Alternar entre os jogadores.
- Verificar se a posição escolhida está livre.
- Verificar quando um jogador vencer a partida.
- Declarar empate caso todas as posições estejam preenchidas sem vencedores.

O jogo pode ser representado como uma lista de três elementos, onde cada elemento também é uma lista com três elementos. 
Exemplo de tabuleiro:
```text
X | O |  
--+---+---  
  | X | X  
--+---+---  
  |   | O 
```

Posições mapeadas como no teclado numérico:
```text
7 | 8 | 9  
--+---+---  
4 | X | 6  
--+---+---  
1 | 2 | 3  
```

---

## 💡 Objetivo do exercício

- Criar um jogo da velha para dois jogadores no console.  
- Aprender a manipular listas de listas para representar o tabuleiro.  
- Praticar alternância entre jogadores e verificação de posições livres antes de jogar.  
- Implementar lógica de verificação de vitória e empate (deu velha).  
- Reforçar o uso de índices e joins para imprimir o tabuleiro de forma dinâmica.  

---

## 🧠 Explicação do raciocínio

- O tabuleiro é representado como uma lista de listas, cada sublista sendo uma linha do desenho, permitindo alterar elementos individualmente.  
- Cada posição do tabuleiro corresponde a um número de 1 a 9, mapeado como no teclado numérico, facilitando a entrada do jogador.  
- A cada jogada, o programa verifica se a posição escolhida está livre antes de atualizar o tabuleiro.  
- Os jogadores se alternam usando uma lista `jogadores` e o método `pop(0)` para controlar a vez.  
- A lógica de vitória é verificada combinando elementos das linhas, colunas e diagonais, e desenhando linhas ou símbolos para indicar a vitória no tabuleiro.  
- Se todas as posições forem preenchidas e ninguém vencer, o jogo declara empate ("Deu velha!").  
- A prática de manipular listas de listas e usar `"".join(linha)` para imprimir cada linha reforça o aprendizado de como combinar estruturas de dados e saída formatada no console.  

---

## 🖥 Exemplo de execução

```text
7 | 8 | 9  
--+---+---  
4 | 5 | 6  
--+---+---  
1 | 2 | 3  

Em qual posicao deseja colocar o X (de 1 a 9): 5  

7 | 8 | 9  
--+---+---  
4 | X | 6  
--+---+---  
1 | 2 | 3  

Em qual posicao deseja colocar o O (de 1 a 9): 1  

7 | 8 | 9  
--+---+---  
4 | X | 6  
--+---+---  
0 | 2 | 3  
```
