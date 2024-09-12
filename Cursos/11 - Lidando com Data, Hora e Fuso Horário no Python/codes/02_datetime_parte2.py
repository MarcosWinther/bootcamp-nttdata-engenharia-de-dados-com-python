# Essa forma é mais comum de usar do que o exemplo anterior
from datetime import date, datetime, time

data = date(2024, 9, 11)
print(data)

# today(): informa a data atual
print(date.today())

data_hora = datetime(2024, 9, 11, 11, 10, 30)
print(data_hora)

print(datetime.today())

# hora
hora = time(12, 20, 0)
print(hora)