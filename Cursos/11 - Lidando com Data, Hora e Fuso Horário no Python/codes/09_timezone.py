from datetime import datetime, timedelta, timezone

# Usando o exemplo Oslo
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Usando o exemplo Brasil - São Paulo
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), 'BRASIL-SP'))

print(data_oslo)
print(data_sao_paulo)