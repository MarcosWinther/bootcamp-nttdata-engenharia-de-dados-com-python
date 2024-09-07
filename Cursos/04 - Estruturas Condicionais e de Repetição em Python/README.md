# 📖 Estruturas Condicionais e de Repetição em Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Identação

- Identação na programação é uma forma de deixar o código mais legível e fácil para manutenção.
- No Python, a identação vai determinar onde o bloco se inicia e onde ele termina.

### Bloco de comando
- Em outras linguagens de programação o início ou fim do bloco utilizam palavras reservadas ou caratcteres.

### Espaços em branco no Python
- Como boa prática é recomendadp utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco de código deverá adicionar 4 espaços em branco.

<br>


## 📝 Estruturas Condicionais

- Estruturas Condicionais permitem que um programa executem comandos através das condições estabelecidas, representadas por condiçoes lógicas **(True/False)**;
- Palavras reservadas utilizadas nas estruturas condicionais: ``if``, ``elif`` e ``else``.

| Estrutura condicional | Explicação                                                           |
|:---------------------:|:-------------------------------------------------------------------- |
|          if           | Só será executado caso a expressão seja verdadeira.                  |
|         if/else       | Caso seja verdadeiro o ``if`` é executado, senão o else é executado. |
|          elif         | Quando queremos usar mais desvios, utilizamos a palavra reservada``elif``. Essa palavra reservada refere-se a uma nova expressão lógica, caso seja verdaeira o bloco do código de ``elif`` é executado.|

````sh
Evite utilizar grandes estruturas condicionais, pois isso aumentará a complexidade de código que você está implementando!
````


### If aninhado

- Podemos adicionar mais blocos de ``if/elif/else`` dentro do outro bloco ``if/elif/else``, mas lembrando de não utlizar grandes quantidades de estruturas condicionais para não aumentar a complexidade do código.


### If ternário

- Permite escrever a condição em uma única linha;
- Ele é composto por três partes:
  - Primeira parte é o retorno verdadeiro caso seja **True** o resultado da expressão lógica;
  - A segunda parte é a expressão lógica;
  - E a última parte é o retorno falso caso a condição da expressão não for atendida **(False)**.

<br>


## 📝 Estruturas de Repetição

- Estruturas de repetição são estruturas que realizam repetições de um trecho de código por um determinado número;
- Esse númeroe pode ser conhecido previamente ou obtido por uma expressão lógica.

| Comando | Explicação do comando                    |
|:-------:|:-----------------------------------------|
|   for   | Usado para percorrer um objeto interável. Faz sentido sua utilização quando sabemos o número exato de vezes que o bloco de código deve ser executado , ou quando queremos percorrer um objeto interável. |
|  while  | Usado para repetir um bloco de código várias vezes. Faz sentido sua utilização quando não sabemos a quantidade exata de executação de um bloco de código. |

### Função range

- Range é uma função built-in do Python;
- Produz uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo);
- Se usarmos range(i,j) será produzido: ``i, i+1, i+2, ..., j-1``;
- Essa função recebe 3 argumentos
  - Stop (obrigatório);
  - Start (opcional);
  - Step (opcional);



