# 📖 Primeiros passos com DAX e Cálculos com Power BI

## 📝 O que é DAX?

- Segundo a Microsoft:
	- "O DAX é uma coleção de funções, operadores e constantes que podem ser usados em uma fórmula, ou expressão, para calcular e retornar um ou mais valores".

### Medidas

- Úteis para operar linha por linha;
- Medidas rápidas ou/e com DAX;
- Calculadas sob demanda.

``As medidas são calculadas com base nos filtros usados pelo usuário do relatório. Esses filtros são combinados para criar o contexto do filtro.``


### Medidas DAX:

- Compilar medidas rápidas;
- Criar colunas calculadas;
- Usar a **DAX** para compilar medidas;
- Descobrir de que modo o contexto afeta as medidas **DAX**.
- Usar a função **CALCULATE** para manipular filtros.
- Implementar a inteligência de dados temporais usando a **DAX**.


### Desvantagem de utilizar o DAX

- Não é bem compactada quanto aos outros métodos;
- Influencia no tamanho do arquivo **.pbix**.

``Use o DAX quando não houver outra alternativa!``


### Colunas

- Será armazenado no arquivo **.pbix**;
- Cada coluna aumenta o espaço usado.

``Aumento de espaço que possivelmente aumentará o tempo de atualização.``


#### Coluna Calculada

- Coluna não original.
- Agregação e funções matemáticas.
- DAX.
- Um valor para cada linha chamada.


#### Coluna Personalizada

- 3 formas de criar:
	- Criando a coluna de origem na obtenção dos dados, por exemplo: obtendo os dados através consulta utilizando SQL;
	- Criando com Power Query.
	- Criando a coluna calculada usando DAX.
	
``Você pode criar uma coluna calculada ao efetuar pull dos dados obtidos em uma fonte de dados.``


### Entendendo Contexto com DAX

#### Contexto

- Contexto afeta as medidas DAX;
- Mesma medida com resultados diferentes.

``Dados afetados por filtros aplicados as tabelas dinâmicas, relações entre tabelas e filtros de fórmulas.``


#### Tipos de contexto

- Existem diferentes tipos de contextos:
	- **Contexto de linha:**
		- O contexto pode ser considerado a linha atual;
		- Medida com valores relacionados a linha atual.
		- O contexto de linha segue automaticamente as relações entre tabelas para determinar quais linhas nas tabelas relacionadas estão associadas à linha atual.
	- **Contexto de várias linhas:**
		- Funções de interação de cálculos em uma tabela;
		- Com várias linhas e contextos de linhas atuais
	- **Contexto de consulta:**
		- Se refere ao subconjunto de dados recuperados implicitamente para uma fórmula.
	- **Contexto de filtro:**
		- Dentro desse contexto estou especificando **restrições** de filtro aos dados;
		- Vou analisar/enxergar os dados de acordo com esses filtros.
		- Aplicado sobre outros contextos.
		- Posso adicionar expressões de filtros a expressão.
	
``O contexto permite executar análise dinâmica, na qual os resultados podem ser alterados para refletir a seleção atual de linha ou células, além de qualquer dado relacionado.``


#### Contexto em fórmulas

- Verificação das fórmulas
	- Sintaxe DAX e tabelas envolvidas
	
- Contexto:
	- Tabelas;
	- Filtros;
	- Relacionamentos.
	
``Contexto complexo dificulta soluções de erros envolvendo  estes cenários.``

- Exemplos:
	- **RELATED:**
		- Expande o contexto da lina atual incluindo valores de linha relacionada.
	- **FILTER:**
		- Linhas a serem incluídas no contexto atual.
	- **ALL:**
		- Contexto dentro de uma fórmula.
	- **ALLEXCEPT:**
		- Remove os filtros exceto o especificado.
	- ** EARLIER & EARLIEST:**
		- Varredura em Loop as tabelas envolvidas nos cálculos;
		- Envolve conceitos de recursividade e loops.
		- ** EARLIER:**
			- Cálculos aninhados com valor de entrada;
			- Execução de cálculos com base.
		- ** EARLIEST:**
			- Retorna o valor atual da coluna especificada em uma etapa de avaliação externa da coluna especificada.
			
<br>	
	
	
## 📝 Função X

- Funções de iterator.
- Melhor desempenho e menor espaço.
- **SUM, COUNT, MIN** -> **SUMX, COUNTX, MINX**

<br>	
	
	
## 📝 Recursos do DAX

- Modificação de relacionamentos
	- Padrão: **USERRELATIONSHIP**.

	
### O que é USERRELATIONSHIP?

- Especifica o relacionamento durante o cálculo da medida.
