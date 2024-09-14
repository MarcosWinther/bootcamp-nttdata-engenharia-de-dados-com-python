class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

pessoa = Pessoa.criar_de_data_nascimento(1996, 10, 10, "Marcos")
print(pessoa.nome, pessoa.idade)

print(Pessoa.e_maior_idade(16))
print(Pessoa.e_maior_idade(28))