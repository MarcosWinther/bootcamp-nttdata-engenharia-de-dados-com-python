# Desafio bicicletaria

## self: representa a instância do objeto

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
    
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmmmm...")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta("preta", "caloi", 2023, 700, 18)

print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

caloi.correr() # equivalente a essa chamada => Bicicleta.correr(caloi)
caloi.buzinar()
caloi.correr()

print(caloi)


