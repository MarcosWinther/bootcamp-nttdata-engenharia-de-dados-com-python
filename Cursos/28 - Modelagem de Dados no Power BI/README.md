# 📖 Modelagem de Dados no Power BI

## 📝 Modelagem

### Vantagens ter um bom modelo de dados:
- A exploração de dados é rápida;
- As agregações são mais simples de criar;
- Os relatórios são mais precisos;
- A escrita de relatórios leva menos tempo;
- Os relatórios são mais fáceis de manter no futuro.

``Busque a simplicidade!``


### Modelo Menor
- Executado mais rápido;
- Fácil de entender;
- Menor espaço dedicado.

``Não é uma tarefa trivial!``

<br>


## 📝 Power Query

### Start Schema

- Mais indicado para sistemas analíticos;
- Eficiente na recuperação de dados.
- **Casamento perfeito: Power BI e Start Schema.**

<br>


## 📝 Tabelas e Legibilidade

### Vantagens de tabelas simples:

- Navegabilidade de coluna e de tabela amigável para usuário;
- Ter relações de boa qualidade entre tabelas que fazem sentido.
- Ter tabelas mescladas ou acrescentadas para simplificar as tabelas em suas estruturas.

<br>


## 📝 Hierarquia de Dados

- A **"hierarquia de dados"** refere-se à maneira como as informações são organizadas em diferentes níveis de importância ou relacionamento. 
- Isso significa que os dados são estruturados de forma que alguns elementos tenham prioridade sobre outros ou que certos dados dependam de outros.
- Em termos simples:

	- **Ordem de prioridade:** Alguns dados são mais importantes que outros.
	- **Relação de subordinação:** Alguns dados dependem de outros para fazer sentido.
	- **Graus sucessivos:** Existem níveis diferentes, como numa pirâmide, onde os dados no topo têm mais poder ou importância, e os dados na base são subordinados a esses.

- Um exemplo comum disso são as pastas e subpastas em um computador: a pasta principal é o nível mais alto, e as subpastas são organizadas hierarquicamente abaixo dela.

### Outra definição:

- Organização fundada sobre uma ordem de prioridade entre os elementos de um conjunto ou sobre relações de subordinação entre os membros de um grupo, com graus sucessivos de poderes, de situação e de responsabilidades.


### Hierarquia Pai/Filho

- Segundo a Microsoft:
	- "O processo de exibição de vários níveis filhos com base em um pai de nível superior é conhecido como nivelar a hierarquia".

- Ou seja, a "Hierarquia Pai/Filho" refere-se a uma estrutura de dados onde os elementos estão organizados de forma que um elemento superior (pai) pode ter vários elementos subordinados (filhos). 
- Cada "filho" está diretamente relacionado a um único "pai", criando uma relação clara de dependência ou subordinação.

#### No contexto da explicação da Microsoft:

- Quando a Microsoft diz "nivelar a hierarquia", eles se referem ao processo de exibir vários níveis subordinados (filhos) com base em um único nível superior (pai). 
- Isso significa que, partindo de um ponto de origem (o pai), você pode "desdobrar" os níveis filhos para ver a estrutura completa que depende daquele elemento.
- Exemplo visual: Imagine uma organização onde há um gerente (pai) e vários funcionários subordinados a ele (filhos). Se você "nivelar a hierarquia", significa que você vai exibir o gerente e, logo abaixo dele, todos os funcionários que estão subordinados, e assim por diante, com níveis adicionais, como subordinados dos subordinados.

``A ideia é mostrar claramente essa relação de dependência entre os diferentes níveis de dados, facilitando a visualização da estrutura.``

<br>


## 📝 Granularidade de Dados

### Definição

- A granularidade de dados é o nível de detalhes que é representado nos dados.
- **Atenção a Granularidade do seu projeto!**
	- **Problema:** impacto no desempenho do relatório no Power BI.

<br>


## 📝 Relembrando Conceitos de Relacionamentos

### Relação muitos para um ou um para muitos

- **Relação muitos para um:** (*:1)
- **Relação um para muitos:** (1:*)
- Tem muitas instâncias de um valor em uma coluna que estão relacionadas a uma outra;
- Descreve a direcionalidade entre as tabelas fatos e de dimensões.
- Esse é o tipo mais comum de direcionalidade e é o padrão do Power BI quando você está criando relações automaticamente.


### Relação (1:1)

- Descreve uma relação na qual apenas uma instância de um valor é comum entre duas tabelas.
- Requer valores exclusivos em ambas as tabelas.
- **Não é recomendável:** informações redundantes!
- Combinar as tabelas é uma prática mais recomendável.


## Relação (N:M)

- Descreve uma relação em que muitos valores estão em comum entre as duas tabelas.
- Não requer valores exclusivos em nenhuma das duas tabelas em uma relação.
- **Não é recomendável:** a falta de valores exclusivos gera ambiguidade e os usuários talvez não saibam qual coluna de valores está se referindo a quê.

<br>


## 📝 Desafios na Modelagem de Dados

- **Problemas com ciclos:**
	- Dependência de relação.
	- Difícil de gerenciar;
	- Dificultam o entendimento das relações.