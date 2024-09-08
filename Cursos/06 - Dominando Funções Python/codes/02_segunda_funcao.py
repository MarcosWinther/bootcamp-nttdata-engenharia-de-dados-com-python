def calcular_numeros(numeros):
    return sum(numeros)

print(calcular_numeros([2, 4, 6, 10, 12, 14, 16, 18, 20]))

def antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(antecessor_e_sucessor(39))
