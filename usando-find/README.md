# 🐍 Usando a função `find()` em Strings

## 📝 Enunciado
Escreva um programa que leia duas strings.  
Verifique se a **segunda string ocorre dentro da primeira** e imprima a **posição de início** da ocorrência.

**Exemplo:**

1ª string: AABBEFAATT  
2ª string: BE  
Resultado: BE encontrado na posição 3 de AABBEFAATT


---

## 🎯 Objetivo
Aprender a utilizar a função **`.find()`** para **buscar substrings dentro de uma string** e trabalhar com o resultado retornado.

---

## 💡 O que este exercício ensina
- O método `.find()` retorna o **índice da primeira ocorrência** da substring (ou `-1` se não for encontrada).  
- Como **verificar se uma substring existe** em outra string antes de tentar manipulá-la.  
- A diferença entre **índice (base 0)** e **posição (base 1)** para exibir resultados ao usuário.  
- Como usar **fatiamento (`string[indice:]`)** para mostrar o texto a partir de uma posição.

---

## 🚀 Código da solução

O código completo está disponível em [`main.py`](./main.py).

---

## 🧩 Exemplo de execução
Digite a primeira palavra, frase ou letras: AABBEFAATT  
Digite a segunda palavra, frase ou letras: BE  

encontramos (BE, o segundo objeto) no primerio objeto digitado  
ele esta localizado na 3º posicao  
o primerio obejto é AABBEFAATT  
apartir da posicao 3º, temos BEFAATT