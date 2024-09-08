def somar_valores(a, b):
    return a + b

def subtrair_valores(a, b):
    return a - b

def multiplicar_valores(a, b):
    return a * b

def dividir_valores(a, b):
    return a / b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado dos números {a} e {b} da operação escolhida é {resultado}")

exibir_resultado(4, 2, somar_valores)
exibir_resultado(6, 2, subtrair_valores)
exibir_resultado(10, 2, multiplicar_valores)
exibir_resultado(80, 2, dividir_valores)

# Atribuir uma função a uma variável
somar = somar_valores(10, 10)

print(somar)