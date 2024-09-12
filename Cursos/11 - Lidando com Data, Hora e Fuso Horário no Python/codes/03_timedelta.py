import datetime

d = datetime.datetime(2024, 10, 3, 12, 20)

# Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)