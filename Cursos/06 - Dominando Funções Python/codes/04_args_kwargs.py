# args

def soma_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = soma_todos(1, 2, 3, 4, 5)
print(resultado)

#----------------

# kwargs

def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

exibir_informacoes(nome="João", idade=30, cidade="São Paulo")

#-----------------------

# Combinando args e kwargs

def funcao_exemplo(a, b, *args, **kwargs):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

# Chamada da função
funcao_exemplo(1, 2, 3, 4, 5, nome="Ana", idade=28)