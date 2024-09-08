# 📖 Dominando Funções Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Funções

- É um bloco de código identificado por um nome e esse nome é o seu identificador;
- A função pode receber uma lista de parâmetros.
- Os parâmetros podem ou não ter valores padrões;
- Esses parâmetros são considerados como as entradas da função e o retorno é a saída;
- Utilizar função possibilita reaproveitamento de código e torna o código mais legível.
  
````
Programar baseado em funções é o mesmo que dizer que estamos programando de maneira estruturada.
````


### Retornando valores

- Para retornar um valor utilizamos a palavra reservada ``return``;
- Toda função Python retorna ``None`` por padrão;
- Uma grande diferença de Python com as demais linguagens de programação, que uma função no Python pode retornar mais de um valor.


### Argumentos nomeados

- Funções também podem ser chamadas usando argumentos nomeados no formato **chave=valor**;


### Args e kwargs

- Podemos combinar parâmetros obrigatórios com args e kwargs;
- Quando são utilizados (*args, **kwargs), o método recebe os valores como tupla e dicionário respectivamente.


### Parâmetros especiais

- No Python, por padrão, os argumentos podem er passador por uma função tanto por posição quanto pelo nome;
- Para uma melhor legibilidade e desempenho:
  - Restringir a maneira como os argumentos são passados;
  - Isso facilita para o programador que só olhará a definição da função para determinar se os objetos são passados **por posição**, **por posição e nome** ou **por nome**.


### Objetos de primeira classe

- Em Python, tudo é objeto;
- Funções também são objetos, tornando-se objetos de primeira classe;
- Podemos:
  - Atribuir funções a variáveis;
  - Passá-las como parâmetro para funções;
  - Usá-las como valores em estruturas de dados (listas, tuplas, dicionários etc);
  - Usar como valor de retorno para uma função (closures).


### Escopo global e local
- **Escopo local:** contexto que existe dentro de uma função. As variáveis definidas dentro de uma função são acessíveis dentro dessa função e não fora dela;
- **Escopo global:** as variáveis são acessíveis em qualquer parte do código, pois as variáveis foram definidas fora de qualquer função.

````
Não é uma boa prática, mas podemos usar na linguagem Python uma variável de escopo global dentro de uma função utilizando a palavra reservada global.
````
