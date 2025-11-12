# 🎯 Modificando o Jogo da Forca: mostrar a palavra secreta ao perder

## 📝 Enunciado
Modifique o jogo da forca de forma que, caso o jogador perca, o programa **revele a palavra secreta**.


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

## 🎯 Objetivo
- Aprender a manipular **loops `while`**, listas e strings para criar um jogo interativo.  
- Implementar **verificações de tentativas repetidas**.  
- Praticar **construção dinâmica da palavra secreta** com `_` para letras não descobertas.  
- Adicionar **feedback visual** usando múltiplos prints para mostrar o estado do boneco.  

---

## 💡 O que este exercício ensina
- Como criar um **loop principal do jogo** que termina ao acertar a palavra ou cometer 6 erros.  
- Uso de listas (`digitados` e `acertos`) para controlar o histórico de letras.  
- Construção de uma **palavra "oculta"** mostrando apenas letras acertadas.  
- Implementação de **condições para mostrar o estado do boneco** com múltiplos prints.  
- Mostrar a palavra secreta quando o jogador perde, dando **feedback completo**.  
- **Múltiplos prints intencionais**: alguns para o boneco, alguns para mostrar a palavra e acertos, reforçando aprendizado de lógica e manipulação de strings.  

---

## 🚀 Código da solução
O código completo está disponível em [`forca-palavra-secreta.py`](./forca-palavra-secreta.py).

---

## 🧠 Explicação do raciocínio
1. Lemos a palavra secreta do usuário e "limpamos a tela" com vários `print()`.  
2. Criamos listas `digitados` e `acertos` e variável `erros` para controlar o jogo.  
3. No loop principal:  
   - Construímos a palavra atual mostrando `_` para letras não descobertas.  
   - Verificamos se o jogador acertou todas as letras.  
   - Solicitamos uma tentativa e verificamos se já foi digitada.  
   - Atualizamos listas e contagem de erros.  
   - Atualizamos a visualização do boneco da forca usando prints condicionais.  
4. Caso o jogador cometa 6 erros, o jogo termina e **revela a palavra secreta**.

---

## 🧩 Exemplo de execução

Digite a palavra secreta: python  
_____   
digite uma letra: a  
voce errou!  
X==:==  
X  :    
X
X
===========  
...  
enforcado  
a palavra era:   
python  
