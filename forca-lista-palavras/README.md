# 🎯 Jogo da Forca com Lista de Palavras

## 📝 Enunciado
Modifique o programa da forca (do exercício anterior) de forma que:  
- O jogo utilize uma **lista de palavras** no início.  
- O usuário informa um número, e o programa calcula o índice da palavra a usar pela fórmula:  

    indice = (numero * 776) % len(lista_de_palavras)

---

## 💡 Objetivo do exercício
- Aprender a **selecionar elementos de uma lista usando um cálculo**.  
- Reforçar o uso de **loops while**, listas e strings para criar um jogo interativo.  
- Implementar **verificações de tentativas repetidas** e feedback visual com múltiplos prints.  
- Aplicar o conceito de **combinar listas e strings** ao mesmo tempo (listas para `acertos` e strings para `senha`).  
- Mostrar a palavra secreta caso o jogador perca.  

---

## 🚀 Código da solução
O código completo está disponível em [`main.py`](./main.py).  


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
