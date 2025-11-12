# ✨ Gerando Strings com Caracteres Únicos usando `.join()` e `.rfind()`

## 📝 Enunciado
Escreva um programa que leia duas strings e gere uma terceira com **apenas os caracteres que aparecem em uma delas**, ou seja, **excluindo os caracteres comuns**.

**Exemplo:**

1ª string: CTA   
2ª string: ABC  
Resultado (3ª string): BT  

> A ordem dos caracteres da terceira string **não é importante**.

---

## 🎯 Objetivo
Praticar a **manipulação de strings** para identificar **caracteres exclusivos** de cada string e gerar uma nova string.  
Este exercício reforça o uso de:
- `.join()` para transformar listas em strings  
- `.rfind()` para localizar caracteres  
- Estruturas de decisão (`if`) para filtrar dados

---

## 💡 O que este exercício ensina
- Como percorrer duas strings e comparar seus caracteres.  
- Como **construir listas e strings** com caracteres exclusivos.  
- Diferença entre **concatenação direta (`+=`)** e **uso de `.join()`**.  
- Como usar métodos de string como `.rfind()` para verificar a existência de um caractere.  
- Conceito de **diferença de conjuntos**, aplicado manualmente em strings.

---

## 🚀 Código da solução
O código completo está disponível em [`caracteres-unicos.py`](./caracteres-unicos.py).

---

## 🧠 Explicação do raciocínio
1. O programa lê duas strings (`um` e `dois`).  
2. Percorre cada caractere de `um` e adiciona à nova string se **não estiver presente em `dois`**.  
3. Percorre cada caractere de `dois` e adiciona se **não estiver presente em `um`**.  
4. Constrói a terceira string usando **listas e `.join()`**.  
5. Uma segunda abordagem usa `.rfind()` para checar se o caractere está ausente na outra string, reforçando a lógica.

---

## 🧩 Exemplo de execução

Digite a primeira palavra, frase ou letras: CTA  
Digite a segunda palavra, frase ou letras: ABC  

BT  
BT  
BT  
BT 

> 💡 Observação:
> Neste exercício foram aplicadas **duas abordagens principais**:
> 1. Concatenar caracteres diretamente em uma string vazia (`+=`)  
> 2. Guardar os caracteres em uma lista e depois usar `.join()`  
> 
> Além disso, foram testados **vários tipos de print**, como imprimir direto o resultado de `.join()`, ou a string acumulada.  
> Por isso aparecem **quatro prints no código**: é intencional, para comparar resultados e reforçar o aprendizado sobre diferentes formas de construir e exibir strings em Python.
