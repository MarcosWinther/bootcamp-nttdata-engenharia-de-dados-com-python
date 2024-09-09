numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # Atribuindo valores na nova lista com dados existentes de outra lista

print(numeros)
print(pares)

# Outra forma:
impares = [numero for numero in numeros if numero % 2 == 1]

print(impares)

# Outro exemplo
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)
