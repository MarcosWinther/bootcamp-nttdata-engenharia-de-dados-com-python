class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self.ano_nascimento
    
marcos = Pessoa("Marcos", 1996)
print(f"Nome: {marcos.nome} \tIdade: {marcos.idade}")