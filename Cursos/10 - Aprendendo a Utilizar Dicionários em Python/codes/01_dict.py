# Criando dicionário com {}
pessoa = {"nome": "Marcos Winther", "idade": 28}

print(pessoa)

pessoa["telefone"] = "64 9 1234-5564"

print(pessoa)

# Criando dicionário com o construtor dict
pessoa_2 = dict(nome="Thais", idade=27)

print(pessoa_2)

# ------------------------------------------------------------------

print(pessoa["nome"])

# Retribuindo novos valores as chaves do dicionário pessoa


pessoa["nome"] = "Celia"
pessoa["idade"] = 55
pessoa["telefone"] = "64 9 5467-8744"

print(pessoa)