# 📖 Otimização de Modelo de Dados com Foco em Desempenho no Power BI

## 📝 Otimização

- Realizações de modificações no estado atual do modelo de dados a fim de executar suas operações com maior eficiência.
- Desta forma, aumentamos seu desempenho.


### O que impacta o baixo desempenho no relatório?

- Lentidão no carregamento;
- Demora na atualização dos visuais.


### Motivos de um relatório com mau desempenho

- Modelagem inadequada;
- Mau uso da linguagem DAX;
- Combinação dos dois motivos citados acima;


### Vantagens da  Otimização

- Melhor experiência do usuário;
- Desempenho e bons resultados;
- Cliente satisfeito.


### Processos de Otimização

- Garantir que os tipos de dados corretos sejam usados;
- Excluir colunas e linhas desnecessárias;
- Evitar valores repetidos;
- Substituir colunas numéricas por medidas;
- Usar variáveis para aprimorar o desempenho e solucionar problemas;
- Reduzir cardinalidades;
- Analisar metadados do modelo;
- Resumir dados sempre que possível;
- Criar e gerenciar agregações.


### Fatores que influenciam no Desempenho

``Facilidade x Disponibilidade``

- Acesso aos Dados;
- Tempo de carregamento;
- Permissão do acesso.


### Resolvendo problemas de Otimização

#### Verificando Visuais

- Melhorar o desempenho;
- Mínimo impacto na experiência do usuário;
- Menos visuais -> mais desempenho.


#### Verificando DAX

- Tempo de execução de consulta;
- Performance Analyser.
- Referência: 120 milissegundos.

#### Verificando Modelagem de Dados

- Visuais com bom desempenho;
- DAX com execução rápida.
- Provável: relações, colunas ou metadados.
- **Pontos de atenção:**
	- Verifique as relações e cardinalidades;
	- Delete as colunas desnecessárias;
	- Preferência de exclusão: na importação;
	- Use o Power Query quando necessário.


### Técnicas para redução de dados:

- Remover colunas desnecessárias;
- Remover linhas desnecessárias;
- Otimizar tipos de dados de coluna;
- Agrupar e resumir;
- Preferência por colunas personalizadas;
- Desabilitar data/hora automática.