# Desafio bicicletaria

## self: representa a instância do objeto

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmmmm...")

caloi = Bicicleta("preta", "caloi", 2023, 700)

print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

caloi.correr()
caloi.buzinar()
caloi.correr()


