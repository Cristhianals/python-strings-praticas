# 🧩 Usando as funções `join()` e `find()` em Strings

## 📝 Enunciado
Escreva duas strings e gere uma terceira com os **caracteres comuns** às duas strings lidas.

**Exemplo:**

1ª string: AAACTBF  
2ª string: CBT  
Resultado: CBT  


> A ordem dos caracteres da string gerada **não é importante**, mas deve conter todas as letras que aparecem em **ambas** as strings.

---

## 🎯 Objetivo
Aprender a identificar **caracteres comuns entre duas strings** e utilizar funções como **`.join()`** e **`.find()`** para montar novas strings a partir desses resultados.

---

## 💡 O que este exercício ensina
- Como percorrer uma string com `for` e comparar caracteres com o operador `in`.  
- Como construir uma nova string com **concatenação (`+=`)** ou com **`.join()`** (forma mais eficiente).  
- Como usar **`.find()`** para verificar se um caractere está presente em outra string.  
- Diferença entre **listas e strings** — e como transformar uma lista em string usando `.join()`.

---

## 🚀 Código da solução
O código completo está disponível em [`usando-join-e-find.py`](./usando-join-e-find.py).

---

## 🧠 Explicação do raciocínio
1. O programa lê duas strings fornecidas pelo usuário.  
2. Percorre cada caractere da primeira string (`um`) e verifica se ele existe na segunda (`dois`).  
3. Se sim, adiciona esse caractere a uma lista (`igual`) e também a uma string (`iguais`).  
4. Depois, usa `"".join(lista)` para **juntar os caracteres** e formar uma nova string com as letras comuns.  
5. Uma segunda abordagem usa `.find()` para o mesmo propósito, reforçando o aprendizado.

---

## 🧩 Exemplo de execução
Digite a primeira palavra, frase ou letras: AAACTBF  
Digite a segunda palavra, frase ou letras: CBT  

CBT  
CBT  
CBT  
CBT  