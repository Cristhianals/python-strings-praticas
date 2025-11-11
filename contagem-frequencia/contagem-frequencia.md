# 🔢 Contando caracteres em uma string usando `.count()`

## 📝 Enunciado
Escreva um programa que leia uma string e **imprima quantas vezes cada caractere aparece** nela.

**Exemplo:**

Entrada: TTAAC  
Saída:  
T 2x  
A 2x  
C 1x  

---

## 🎯 Objetivo
Aprender a contar **frequência de caracteres** em uma string, usando funções nativas de Python como **`.count()`**, e controlar a impressão para **não repetir caracteres**.

---

## 💡 O que este exercício ensina
- Como percorrer uma string com `for` e `enumerate()`.  
- Uso do método **`.count()`** para contar ocorrências de um caractere.  
- Como usar slicing (`p[:l]`) para **evitar imprimir caracteres já contados**.  
- Controle de fluxo básico com `if` e lógica para não repetir resultados.

---

## 🚀 Código da solução
O código completo está disponível em [`main.py`](./main.py).

---

## 🧠 Explicação do raciocínio
1. Lemos a string do usuário (`p`).  
2. Usamos `enumerate()` para percorrer cada caractere e seu índice.  
3. Para cada caractere, usamos `.count()` para descobrir quantas vezes ele aparece.  
4. O `if not b in p[:l]` garante que **não contemos novamente um caractere já processado**.  
5. Imprimimos o resultado no formato `{caractere} aparece {n} vezes`.

---

## 🧩 Exemplo de execução

Digite a primeira palavra, frase ou letras: TTAAC

T aparece 2 vezes  
A aparece 2 vezes  
C aparece 1 vez  