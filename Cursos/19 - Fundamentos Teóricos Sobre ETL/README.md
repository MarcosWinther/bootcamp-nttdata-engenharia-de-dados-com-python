# 📖 Fundamentos Teóricos Sobre ETL

## 📝 O que é ETL? 

- **Extract:** extração;
- **Transform:** transformação;
- **Load:** carregamento.

### Extract (Extração)

- Essa etapa envolve coletar dados de diferentes fontes;
- **Objetivo:** extrair os dados brutos para ser manipulados na próxima etapa.
- Exemplos de fontes:
	- Banco de Dados SQL ou NoSQL;
	- APIs, como por exemplo APIs RESTful;
	- Arquivos como CSV, Excel, JSON;
	- Logs de sistemas;
	- Data lakes.


### Transform (Transformação)

- Essa etapa envolve a manipulação dos dados extraídos para transformálos em um formato adequado para a análise de uso. 
- Isso pode incluir:
	- **Limpeza de dados:** remover dados duplicados, lidar com dados ausentes, corrigir formatações inconsistentes;
	- **Conversão de formato:** alterar tipos de dados;
	- **Agregação e sumarização:** agrupar dados e calcular médias, somas ou contagens;
	- **Normalização:** ajustar os dados para garantir que estejam em um formato consistente;
	- **Criação de métricas:** gerar novos campos ou métricas a partir dos dados originais.


## Load (Carregamento)

- Considerada a etapa final, onde os dados transformados são armazenados em um destino final;
- Como por exemplo:
	- um data warehouse;
	- um banco de dados relacional;
	- ou em um sistema de **Big Data**(como Hadoop ou Spark).
- Esses dados podem ser usados por cientistas de dados, analistas ou por sistemas  de BI para gerar relatórios, análises e insights.

<br>


## 📝 ELT

- Variação do processo ETL, comum em arquiteturas modernas.
- Solucionam o mesmo problema.
- O processo de ELT é mais ágel em relação ao ETL.
- A principal diferença está na ordem das etapas de transformação e carregamento dos dados:
	- **ETL:** Primeiro os dados são extraídos, depois transformados (limpos, processados, organizados) antes de serem carregados no sistema de armazenamento final.
	- **ELT:** Primeiro os dados são extraídos, depois são carregados diretamente no sistema de armazenamento (data warehouse ou data lake), e só então são transformados no próprio destino.
	
### Processo ETL

- Independência de TI;
- Responsável: profissionais de análise de dados;
- Vantagem: contato direto com regras de negócio.


#### Extract

- Coleta dos dados brutos
- Fontes heterogêneas
- Objetivo: integração posterior


#### Load

- Transferência/carregamento;
- Dados brutos;
- Data warehouse ou repo


#### Transform

- Transformação dos dados;
- Aplicação das análises.

### Vantagens do ELT

- Otimização de tempo;
- Eficiência na implementação de projetos;
- Menor dependência de TI;
- Papel principal dos analistas.

<br>


## 📝 Deferenças: ELT x ETL

### Vantagens ELT

- Tempo de carregamento: Sistemas -> delay;
- Tempo de transformação;
- Tempo de manutenção;
- Complexidade de implementação;
- Limutação de dados;
- Suporte à Data Warehouse;
- Usabilidade.
