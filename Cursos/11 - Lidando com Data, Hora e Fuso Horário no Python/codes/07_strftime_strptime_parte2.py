from datetime import datetime

mascara_ptbr = '%d/%m/%Y - %a - %H:%M'
mascara_en = '%Y/%m/%d %H:%M'

data_hora_atual = datetime.now()
print(data_hora_atual.strftime(mascara_ptbr))
print(type(data_hora_atual))

date_string = "2024/10/2 15:30"
print(type(date_string))

data_convertida = datetime.strptime(date_string, mascara_en)
print(data_convertida)
print(type(data_convertida))