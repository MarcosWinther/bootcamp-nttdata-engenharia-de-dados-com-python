# 📖 Aplicando Encapsulamento em Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Encapsulamento

- O encapsulamento descreve o agrupamentos de dados e métodos que manipulam esses dados em uma unidade;
- Isso restringe o acesso direito a variáveis e métodos, evitando assim a modificação acidental de dados.
- Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

<br>


## 📝 Recursos Públicos e Privados

- Diferente de outras linguagens de programação, no Python não temos palavras reservadas para definir o nível de acsso aos atributos e métodos da classe;
- Porém, usamos convenções no nome do recurso que define se a variável é publica ou privada.


### Público x Privado

- **Público:** pode ser acessado fora da classe;
- **Privado:** seu acesso é somente dentro da classe.


### Público e Privado no Python

- Todos os recursos são públicos, porém usamos a conversão de usar **underline** no início da variável ou método;
- Mesmo usando essa conversão, o interpretador do Python não irá garantir a proteção desse recurso;
  
``Convenção adotada na comunidade: variável ou método iniciandos com **underline**, não manipular o seu valor diretamente ou invocar um método fora do escopo de sua classe``.

<br>


## 📝 Property

- Também conhecido como propriedades.
- No Python, com o atributo **property**, você pode criar atributos gerenciados em suas classes.
- Você pode usar os atributos gerenciados quando precisar modificar sua implementação interna sem alterar a API pública da classe.