# 📖 Fundamentos de Modelagem Dimensional

## 📝 Modelagem Dimensional

### Vantagens:

- Performance;
- Escabilidade;
- Disponibilidade.


### Sistemas de Dados:

- **Modelo transional:** tradicional
	- Fim específico;
	- Cenário otimizado;
	- Suporte a operação;
	- SGBDs.
- **Modelo dimensional:** analítico.
	- Permite redundâncias;
	- Esquema flexível;
	- Foco em análises;
	- Modelo em cubo.


### Modelagem em Cubo

- Características:
	- **Eixos:** representam os componentes do esquema;
	- **Interseção** (linha, coluna, altura): representam medidas e dados do contexto;
	- Visão consolidada de um contexto mais consolidado se comparado a uma tabela;
	- Análises de perspectivas distintas.


### Modelo Transional x Modelo Dimensional: Qual é o melhor?

- Esses modelos coexistem, pois cada sistema tem a sua particularidade.
- **Transional:**
	- Sistemas de vendas;
	- Alta disponibilidade;
	- Confiança na estrutura e restrições.
- **Anático:**
	- Análise x Disponibilidade;
	- Consolidar informações;
	- Análises dos dados.

<br>	
	
	
## 📝 Explorando os Modelos Dimensionais

### Modelo Estrela

- Também conhecido como **Star Schema**;
- Mais difundido dos modelos;
- Conexão das tabelas em forma de estrela, ou seja, a estruturação desse modelo lembra um formato de estrela;
- Chave artificial;
- Dois tipos de tabelas:
	- **Fato (tabela principal):** se relaciona com as demais por meio de junções;
		- Aspectos que compõem o contexto analisado.
	- **Dimensão (detalhes):** possui os detalhes que compõe a tabela fato, detalhes de um aspecto específico.
		- PKs simples e dados exclusivos.


### Modelo Snowflake

- Variação do modelo estrela;
- Tabelas dimensão podem ter junções entre si impondo um nível de normalização.
- **Observação:** A normalização pode comprometer o desempenho do data warehouse.
- Desvantagens: complexidade, pouco espaço, hierarquias.


### Modelo Constelação / Galáxia

- Múltiplas estrelas são relacionadas entre si;
- Tabelas fatos podem compartilhar tabelas dimensão;
- Integra diversos assuntos em um mesmo contexto.

<br>


## 📝 Granularidade dos Dados

- Grão ou granularidade;
- Nível de detalhamento dos dados na tabela fato;
- Maior o grão: menos detalhes;
- Trade-off na definição.
- ** Atenção!**
	- Cuidado com o nível de granularidade, pois quando menor o grão maior será o processamento!
	- Não adianta um modelo perfeito se eu não consigo processar.

<br>


## 📝 Chave Artificial com Start Schema

### Chave artificial

- Chave relacionada ao modelo dimensional;
- Substitui a identificação sem sobreposição;
- Facilita a identificação de registros no modelo atual.


<br>


## 📝 Slowly Changing Dimensions

- Relacionados as mudanças temporais dos dados.


### Tipos:

- **Tipo SCD-0**:
	- Não há modificação;
	- Modo passive;
	- TRUNCATE TABLE: sem histórico, ou seja, vou deletar e realizar a inserção dos dados novamente.
	
- **Tipo SCD-1**:
	- Atualização dos valores;
	- Sem rastreamento de mudanças;
	- UPDATE ou INSERT.

- **Tipo SCD-2**:
	- Preocupação com o histórico;
	- Modos distintos de rastrear as mudanças.
	
- **Tipo SCD-3**:
	- Novos atributos (colunas) são criados;
	- Manter o estado de um atributo específico.
	
- **Tipo SCD-4**:
	- Manutenção do histórico com tabela de histórico;
	- Mesma estrutura.

- **Tipo SCD-6**:
	- Junção dos tipos **1**, **2** e **3** = **6** (somatório).