import datetime

d = datetime.datetime.now()

# Formatando data e hora com o método strftime
print(d.strftime("%d/%m/%Y %H:%M"))

# Convertendo string para datetime utilizando o método strptime
date_string = "30/1/2024 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)
