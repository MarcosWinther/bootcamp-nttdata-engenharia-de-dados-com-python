# 📖 Introdução à Programação Orientada a Objetos (POO) com Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Paradigmas de Programação

- Um paradigma de programação é um estilo de programação;
- É a forma como você solucina um problema através do código.
- Alguns paradigmas de programação:
  - Imperativo ou procedural;
  - Funcional;
  - Orientado a eventos.

- Vamos focar nesse curso no **Paradigma Orientada a Objetos (POO)**.

<br>


## 📝 Paradigma Orientada a Objetos (POO)

- O POO estrutura o código abstraindo problemas em objetos do mundo real;
- Isso facilita o entendimento do código e torna-o mais modular e extensível.
- Os dois conceitos importantes: **classes** e **objetos**.


### Classes

- Uma classe é algo abstrato onde eu defino os comportamentos e as características de um objeto;
- Porém não conseguimos usá-las diretamente, precisamos instanciá-las.


### Objetos

- Os objetos podemos usá-los diretamente, pois o objeto é uma instância da classe;
- Eles possuem as características e os comportamentos já definidos pelas classes.


### Método construtor

- Esse método é sempre executado quando uma nova instância da classe é criada, inicializando o estado do objeto;
- No Python para declarar o método construtor da classe criamos um métodocom o nome "``__init__``".


### Método Destrutor

- Esse método é sempre executado quando uma instância (objeto) é destruída;
- Destrutores não são tão necessários em Python, pois a linguagem tem um coletor de lixo que lida com o gerenciamento de memória automatcamente;
- Para declarar o método destrutor em Python, criamos um método com o nome "``__del__``".