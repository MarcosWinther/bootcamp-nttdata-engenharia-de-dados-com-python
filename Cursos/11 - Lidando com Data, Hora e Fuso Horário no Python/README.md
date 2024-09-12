# 📖 Estruturas Condicionais e de Repetição em Python

``Todos os códigos feitos nesse curso estão na pasta codes! Aqui nesse arquivo segue as anotações realizadas no curso.``

## 📝 Módulo datetime

- Módulo no Python responsável por lidar com datas e horas.
- Esse módulo possui várias classes úteis como ***date***, ***time*** e ***timedelta***.


### Aware and Naive Objects

- **Naive object (Objeto ingênuo):** data que não tem fuso horário, **UTC time**;
- **Aware object (Objeto consciente):** carrega informações de fuso horário.


### Convertendo Datas e Horas

- Para realizar a conversão de datas e horas no Python utilizamos os ***'strftime' (string format time)*** e ***'strptime' (string parse time)***.


### Timezone

- Para trabalhar com data e hora e lidar com fusos horários no Python, temos o módulo ***'pytz'***.
- É uma bilioteca de terceiros.


### Trabalhando com Timezone sem Bibliotecas Externas

- É um pouco mais complexo, mas o Python permite fazer isso com o módulo padrão **datetime**.
