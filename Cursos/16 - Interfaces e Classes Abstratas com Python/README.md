# 📖 Interfaces e Classes Abstratas com Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Variáveis de Classe e Variáveis de Instância

- **Variáveis de classe:** são variáveis definidas dentro de uma classe.

- Todos os objetos nascem com o mesmo número de atributos de classe e de instância.

- **Atributo de instância:** são diferentes para cada objeto (cada objeto tem uma cópia;
- **Atributo de classe:** são compartilhados entre os objetos.

<br>


## 📝 Métodos de Classe e Métodos Estáticos

### Método de Classe: 

- Estão ligados a Classe e não está ligado ao objeto;
- Esses métodos têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.


### Método Estástico

- É um método que não recebe um primeiro argumento explícito;
- Esse método também é vinculado a classe e não ao um objeto da classe;
- Ele não pode modificar ou acessar o estado da classe;
- Está presente em uma classe.


### Método Estático x Método de Classe

|                      Método de Classe                    |                   Método Estático                 |
|:---------------------------------------------------------|:--------------------------------------------------|
| Recebe um primeiro parâmetro que aponta para a classe.   |        Não                                        |
|Pode acessar ou modificar o estado da classe.             | Não pode acessar ou modificar o estado da classe. |


### Utilização do Método de Classe e Método Estástico

- Usamos o método de classe para criar métodos de fábrica, ou seja, um método que retorna instâncias da classe;
- Usamos o método estástico para criar funções utilitárias.

<br>


## 📝 Interfaces

``Importante: Interfaces definem o que a classe deve fazer e não como.``

- O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas.

### Python tem Interface?

- No Python utilizamos classes abstratas para criar contratos;
- Essas classes não podem ser instanciadas.


### Criando Classes com o Módulo ABC

- Por padrão, o Python não fornece classes abstratas.
- O Python vem com o módulo chamado **ABC** que fornece a base para definir classes abstratas.
- **Funcionamento:** o módulo ABC funciona decorando os métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da classe abstrata.
- Um métood só se torna abstrato com o decorador ``@abstractmethod``.