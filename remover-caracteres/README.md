# ❌ Removendo caracteres de uma string usando `not in` e `.join()`

## 📝 Enunciado
Escreva um programa que leia duas strings e gere uma terceira, na qual **os caracteres da segunda string foram retirados da primeira**.

**Exemplo:**

1° string: AATTGGAA  
2° string: TG  
Resultado: AAAA  


---

## 🎯 Objetivo
Aprender a **remover caracteres** de uma string usando lógica de comparação, percorrendo cada caractere e construindo uma nova string, além de **usar listas e `.join()`**.

---

## 💡 O que este exercício ensina
- Como percorrer uma string com `for`.  
- Uso de `if not c in outra_string` para filtrar caracteres.  
- Construir uma nova string concatenando caracteres (`+=`).  
- Alternativamente, guardar os caracteres em uma lista e depois usar `.join()`.  
- Comparar duas abordagens diferentes para reforçar o aprendizado.  
- Por isso, aparecem **múltiplos prints no código**, para mostrar os resultados de cada abordagem.

---

## 🚀 Código da solução
O código completo está disponível em [`remover-caracteres.py`](./remover-caracteres.py).

---

## 🧠 Explicação do raciocínio
1. Lemos as duas strings do usuário (`um` e `dois`).  
2. Percorremos cada caractere de `um`.  
3. Para cada caractere, verificamos se ele **não está presente** em `dois`.  
4. Se não estiver, adicionamos na string `tres` e na lista `ltres`.  
5. Depois, usamos `.join()` para transformar a lista `ltres` em uma string (`goin`).  
6. Por fim, imprimimos tanto `tres` quanto `goin` para comparar os resultados e reforçar o aprendizado.

---

## 🧩 Exemplo de execução

Digite a primeira palavra, frase ou letras: AATTGGAA  
Digite a segunda palavra, frase ou letras: TG  
AAAA  
AAAA  

> 💡 Observação:
> Neste exercício, foram aplicadas **duas abordagens para gerar a string final**:
> 1. Concatenando caracteres diretamente em uma string (`+=`)  
> 2. Guardando caracteres em uma lista e depois usando `.join()`  
> 
> Por isso aparecem **dois prints** no código: é intencional, para comparar resultados e reforçar o aprendizado de diferentes formas de manipular strings em Python.
