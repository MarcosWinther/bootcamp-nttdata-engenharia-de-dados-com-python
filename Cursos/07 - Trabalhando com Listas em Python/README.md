# 📖 Trabalhando com Listas em Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Criando Listas

- No Python as listas podem armazenar qualquer tipo de objeto de maneira sequencial;
- As listas são objetos mutáveis, podendo alterar seus valores após a sua criação;
- Maneiras de criar lista:
  - Utilizando o construtor ***list***;
  - Utilizando a função range no construtor ***list***;
  - Ou colocando os valores separados por vírgula dentro de colchetes "[ ]".


## 📝 Acessando os dados na lista

### Acesso direto

- Podemos acessar os dados da lista através do índice.


### Índice negativo
- Essa forma de acessar a lista você informar índices negativos, sendo que o acesso desses dados serão acessados a partir do último elemento. 
- Exemplo: se eu informar o índice **-1** será acessado o último elemento da lista.


### Listas aninhadas

- O Python, as listas armazenam todos os tipos de objetos;
- Portanto, podemos armazenar uma lista dentro de outra lista;
- Com isso, criamos uma estrutura bidimensionais (tabelas) e acessar esses dados informando os índices de linha e coluna.


### Fatiamento

- Podemos extrair um conjunto de valores de uma sequência;
- Basta informar o índice inicial e/ou final para acessar o conjunto;
- Podemos também informar quantas posições o cursor deve "pular" no acesso.


### Iterar listas

- A forma mais comum de acessar dados de uma lista é utilizando comando **for** da estrutura de repetição.


### função enumerate

- Para saber o índice do objeto dentro do laço **for** utilizamos a função enumerate.

<br>


## 📝 Compreensão de Listas

- A commpreensão de lista através de sua sintaxe curta permite:
  - Criar uma nova lista com base nos valores existentes de outra lista;
  - Gerar uma nova lista com novos valores aplicando mudança em uma lista existente.