class Cachorro:
    def __init__(self, nome, raca, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância da classe.")

    def latir(self):
        print("auau")

def criar_cachorro():
    cachorro = Cachorro("Thor", "Labrador", "Preto", False)
    print(cachorro.nome)
    cachorro.latir()

golden = Cachorro("Nala", "Golden Retriever", "Dourado")
golden.latir()

del golden

criar_cachorro()