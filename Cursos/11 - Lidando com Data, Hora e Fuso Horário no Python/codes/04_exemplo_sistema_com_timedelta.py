# Simulando um tempo de lavagem de carro de um lava jato

from datetime import datetime, timedelta

tipo_carro = 'P' # pode ser P, M ou G
tempo_pequeno = 30 # tempo em minutos
tempo_medio = 45 # tempo em minutos
tempo_grande = 60 # tempo em minutos
data_atual = datetime.now()
data_estimada = 0

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou às {data_atual} e ficará pronto em {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou às {data_atual} e ficará pronto em {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou às {data_atual} e ficará pronto em {data_estimada}')
