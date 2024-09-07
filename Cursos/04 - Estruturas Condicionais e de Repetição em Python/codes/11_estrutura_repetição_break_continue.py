# break com while
while True:
    numero = int(input("Informe um número inteiro: "))

    if numero == 10:
        break

    print(numero)


# break com for
for numero in range(0, 42):

    if numero == 21:
        break

    print(numero, end=" ")

# continue
for numero in range(0, 21):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")

# break: encerra a execução
# continue: pula a execução