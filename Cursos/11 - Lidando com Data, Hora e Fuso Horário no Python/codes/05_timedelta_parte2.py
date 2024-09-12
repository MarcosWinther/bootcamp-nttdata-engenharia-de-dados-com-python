from datetime import date, datetime, time, timedelta

print(date.today() - timedelta(days=1))

resultado = datetime(2024, 9, 11, 12, 10, 30) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())