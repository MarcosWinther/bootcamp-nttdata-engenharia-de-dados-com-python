NUMERO_ESPECIAL = 40

numero = int(input("Digite um número: "))

if numero == NUMERO_ESPECIAL:
    print("Você acertou o número secreto!")
elif (numero >= 30) and (numero < NUMERO_ESPECIAL):
    print("Você quase acertou o número secreto :(")
else:
    print("Você passou longe de acertar o número secreto :(")