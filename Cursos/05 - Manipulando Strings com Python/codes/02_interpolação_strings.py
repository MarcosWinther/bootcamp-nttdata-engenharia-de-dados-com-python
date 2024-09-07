# Old style %

# Lembrado:
# NÃO É RECOMENDADO SUA UTILIZAÇÃO NO PYTHON 3!

# %s para valores Strings
# %d para valores inteiros
# %f para valores flutuantes

nome = "Marcos Winther"
idade = 28
profissao = "programador"
linguagem = "Python"

print("Olá, eu sou %s, tenho %d anos e desejo trabalhar como %s. Atualmente estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#---------------------------

# Método format

print("Olá, sou {}, tenho {} anos e desejo trabalhar como {}. Estou atualmente estudando a linguagem de programação {}.".format(nome, idade, profissao, linguagem))

# Os números representam o índice
print("Nome {1}, idade {0} anos".format(nome, idade))

print("Olá, sou {nome}, tenho {idade} anos e desejo trabalhar como {profissao}. Estou atualmente estudando a linguagem de programação {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Utilizando dicionário
dados = {"nome": "Marcos Winther", "idade": 28}

print("Nome: {nome}, idade: {idade} anos.".format(**dados))

#---------------------------------------------

# f string

print(f"nome: {nome}, idade: {idade}")

saldo = 549.589999

print(f"saldo: R${saldo: .2f}") # .número representa a quantidade de casas decimais
print(f"saldo: R${saldo: 10.2f}") # 10 representa 10 espaços em branco