# 🔄 Substituindo caracteres em uma string usando listas e strings

## 📝 Enunciado
Escreva um programa que leia **três strings** e imprima o resultado da substituição na primeira string,  
substituindo os caracteres da segunda pelos da terceira.

**Exemplo:**

1ª string: AATTCGAA  
2ª string: TG  
3ª string: AC  
Resultado: AAAACCAA  

---

## 🎯 Objetivo
Aprender a:
- Substituir caracteres em uma string com base em outra string.  
- Manipular strings usando **listas** e **concatenando diretamente em uma string**.  
- Lidar com posições e índices usando `enumerate()` e `find()`.  

---

## 💡 O que este exercício ensina
- Como percorrer uma string com `enumerate()`.  
- Como usar `.find()` para localizar a posição de caracteres.  
- Como **substituir caracteres** mantendo o restante da string intacto.  
- Aplicar **duas abordagens ao mesmo tempo**:  
  1. Concatenando caracteres diretamente em uma string (`+=`)  
  2. Guardando caracteres em uma lista e depois usando `.join()`  
- Por isso, aparecem **dois prints** no código: intencional, para comparar os resultados e reforçar o aprendizado.

---

## 🚀 Código da solução
O código completo está disponível em [`substituicao-caracteres.py`](./substituicao-caracteres.py).

---

## 🧠 Explicação do raciocínio
1. Lemos as três strings do usuário (`um`, `dois` e `tres`).  
2. Criamos uma lista (`quarta`) e uma string (`quatro`) para armazenar a substituição.  
3. Para cada caractere da primeira string (`um`):  
   - Se ele estiver na segunda string (`dois`), substituímos pelo caractere correspondente da terceira string (`tres`).  
   - Se não houver posição correspondente, usamos o último caractere de `tres`.  
   - Se o caractere **não estiver na segunda string**, mantemos ele inalterado.  
4. A lista `quarta` é transformada em string usando `.join()`.  
5. Imprimimos tanto a string da lista quanto a string concatenada diretamente (`quatro`) para comparar as duas abordagens.

---

## 🧩 Exemplo de execução

Digite a primeira palavra, frase ou letras: AATTCGAA  
Digite a segunda palavra, frase ou letras: TG  
Digite a terceira palavra, frase ou letras: AC  
AAAACCAA  
AAAACCAA  

> 💡 Observação:
> Neste exercício, foram aplicadas **duas abordagens para gerar a string final**:
> 1. Concatenando caracteres diretamente em uma string (`+=`)  
> 2. Guardando caracteres em uma lista e depois usando `.join()`  
> 
> Por isso aparecem **dois prints** no código: é intencional, para comparar resultados e reforçar o aprendizado de diferentes formas de manipular strings em Python.
