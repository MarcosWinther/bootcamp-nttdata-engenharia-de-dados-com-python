# 📖 Conhecendo a Linguagem de Programação Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``


## 📝 Tipos de dados
- Os tipos de dados servem para definir as características e comportamentos de um valor (objeto) para o interpretador.
- Dependendo o tipo de dado posso realizar operações matemáticas, armazenar caracteres etc.

### Tipos de Dados em Python

| Tipo                           | Python                         |
|:------------------------------:|:------------------------------:|
| **Texto**                      | *str*                          |
| **Númerico**                   | *int, float, complex*          |
| **Sequência**                  | *list, tuple, range*           |
| **Mapa**                       | *dict*                         |
| **Coleção**                    | *set, fronzenset*              |
| **Booleano: (*True/False*)**   | *bool*                         |
| **Binário**                    | *bytes, bytearray, memoryview* |

#### Números interos
- Números inteiros são representados no Python pela classe int e possuem precisão ilimitada.

#### Números de ponto flutuante
- Os números de ponto flutuante sõ usados para representar os números racionais e sua implementação é feita pela classe float.


#### Booleano
- É usado para representar **verdadeiro(True)** ou **falso(False)**, - No Python é implementado pela classe ***bool***.
- Em Python o tipo booleano é uma subclasse de ***int***, sendo qualquer número diferente de **0** representa **verdadeiro** e **0** representa **falso**.
- Exemplos válidos de booleanos: True e False.


## 📝 Modo interativo

- O modo interativo permite o desenvolvedor a escrever o código e ver o resultado na hora;
- Duas formas de iniciar o modo interativo:
  - Chamando apenas o intepretador (Python);
  - Executando o script com a flag "i", por exemplo :
   ````sh
      python -i app.py
   ````


## 📝 Função *dir()*

- Sem argumentos essa função retorna uma lista de nomes para o escopo atual.
- Com argumentos essa função retorna uma lista de atributos válidos para o objeto.


## 📝 Função *help()*

- Invoca o sistema de ajuda integrado que pode fazer buscas em modo interativo ou informar por parâmetro o nome do módulo, função, classe, método ou variável.


## 📝 Variáveis e constantes

### Variáveis
- São valores que podem sofrem modificações no decorrer da execução de um programa.
- A variável pode mudar seus valores através de uma nova atribuição para essa variável, atribuindo um novo valor.
  
``No Python não podemos criar uma variável sem atribuir um valor!``

### Constantes
- São valores imutáveis, que não podem inicializarem sem um valor e permanecem com o mesmo até a finalização do programa.

````
No Python não tem constantes, pois não existe uma palavra reservada para informar que a variável é uma constante!
Nesse caso, é usada a conevenção de criar a variável com todas as letras maiúsculas
````

### Boas práticas:

A nomenclatura das variáveis devem seguir esses padrões:

- O padrão de nomes: snake case;
- Nomes sugestivos;
- Nomes de constantes todo em maiúsculo.


## 📝 Funções entrada e saída

### Função builtin input / Função input

- Função que ler dados de entrada (teclado);
- Recebe um argumento do tipo **string** e exibido na tela para o usuário (saída padrão);
- Essa função lê a entrada, realiza a conversão do dado para string e retorna o valor.

### Função builtin print / Função print

- Função que exibe dados na tela (saída padrão);
- Essa função recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (**sep**, **end**, **file** e **flush**).;
- Todos os objetos são convertidos para string, separados por sep e terminados por end;
- A string final é exibida na tela para o usuário.
