# 🎯 Jogo da Forca com Boneco em Lista de Listas

## 📝 Enunciado
Modifique o programa da forca para que:  
- O boneco seja representado usando **listas de strings** (uma lista por linha).  
- Cada parte do corpo seja desenhada substituindo elementos dessas listas, em vez de controlar via múltiplos prints separados.  
- A lógica de escolha da palavra continua igual ao exercício anterior, usando uma lista de palavras e um número digitado pelo usuário.

Exemplo de manipulação de listas para desenhar:
```python
linha = list("X------")
linha[6] = "|"
"".join(linha)  # resultado: "X-----|"
```

---

## 💡 Objetivo do exercício

- Aprender a manipular listas de listas para desenhar um objeto no console.  
- Reforçar a prática de combinar listas e strings, usando listas para o boneco e strings para representar a palavra oculta.  
- Reutilizar lógica do jogo da forca com listas de palavras e verificação de tentativas.  
- Mostrar a palavra secreta caso o jogador perca.  
- Aplicar conceitos de manipulação de índices e joins em listas para desenhar dinamicamente o boneco.  

## 🧠 Explicação do raciocínio

- O boneco é representado como uma lista de listas, cada sublista sendo uma linha do desenho.  
- Cada erro do jogador substitui um elemento específico nas listas, desenhando progressivamente o boneco.  
- Mantém-se o uso de listas para `acertos` e strings para a palavra oculta (`senha`), reforçando a prática de combinar os dois conceitos.  
- A escolha da palavra continua usando a lista de palavras e o cálculo de índice via número digitado pelo usuário.  
- O desenho final do boneco é feito usando `"".join(linha)` para converter cada linha de volta em string.  
- A prática de múltiplos prints e manipulação de listas foi intencional para **aprender mais sobre Python e manipulação de strings e listas ao mesmo tempo**, como nos exercícios anteriores.

---

## 💡 Código original do exercício
O código fornecido originalmente foi:

```python
palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(50):
    print()
digitados = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "_"
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
        print("X==:==\nX  :  ")
        print("X  0  "if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " \\|  "
        elif erros >= 4:
            linha2 = " \\|/ "
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 = " /   "
        elif erros >= 6:
            linha3 += " / \\ "
        print(f"X{linha3}")
        print("X\n===========")
        if erros == 6: 
            break
```

---

## 🧩 Exemplo de execução

digite um numero: 7  
-----  
digite uma letra: a  
voce errou!  
X==:==  
X  :    
X 0     
X     
X     
X===========  
...  
enforcado  
a palavra era   
banana  




