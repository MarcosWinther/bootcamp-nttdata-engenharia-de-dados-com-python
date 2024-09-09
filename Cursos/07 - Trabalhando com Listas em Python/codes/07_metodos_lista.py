# append(): adiciona um novo elemento na lista

lista = []

lista.append(40)
lista.append([10, 20, 30])
lista.append("Scooby-Doo")
lista.append(10.96)
lista.append("Python")

print(lista)

#--------------------------------------------------------------------------------------------------------

# clear(): Limpa a lista

lista.clear()

print(lista)

#--------------------------------------------------------------------------------------------------------

# copy(): copia dados de uma lista para outra lista

lista = [[10, 20, 30], 40, "Python"]
lista_2 = lista.copy()

print(lista)
print(lista_2)

print(id(lista), id(lista_2)) # Mesmo com dados iguais, aqui demonstra que são elementos diferentes

lista_2[2] = "Scooby-Doo"

print(lista)
print(lista_2) # Só nessa lista ocorrerá a modificação, pois é um objeto diferente da outra lista

#--------------------------------------------------------------------------------------------------------

# count(): determina quantas vezes um determinado objeto aparece na sua lista

animais = ["cachorro", "gato", "coelho", "cachorro"]

print(animais.count("cachorro"))
print(animais.count("gato"))
print(animais.count("coelho"))

#--------------------------------------------------------------------------------------------------------

# extend(): acrescenta mais elementos na lista

linguagens = ["js", "python", "java"]

print(linguagens)

linguagens.extend(["c#", "go", "lua", "c"])

print(linguagens)

#--------------------------------------------------------------------------------------------------------

# index(): informa a primeira ocorrência de um determinado elemento na lista informando seu índice na lista

animacoes = ["Batman", "Scooby-Doo", "Digimon", "Scooby-Doo"]

print(animacoes.index("Scooby-Doo"))

#--------------------------------------------------------------------------------------------------------

# pop(): tira o último elemento da lista.
# O pop utiliza o conceito de pilha: o último a entrar é o primeiro a sair.
# Porém o pop permite que eu elimino também um elemento informando seu índice.

linguagens.pop()
print(linguagens)

linguagens.pop(2)
print(linguagens)

#--------------------------------------------------------------------------------------------------------

# remove(): elimina o objeto informado

linguagens.remove("c#")
print(linguagens)

#--------------------------------------------------------------------------------------------------------

# reverse(): inverte a lista

linguagens.reverse()

print(linguagens)

#--------------------------------------------------------------------------------------------------------

# sort(): ordena a lista

animacoes.pop()
animacoes.extend(["Sakura Card Captors", "Bob Esponja", "Mickey", "Pokemon"])
print(animacoes)

animacoes.sort() # Ordena de maneira crescente
print(animacoes)

animacoes.sort(reverse=True) # Ordena de maneira decrescente
print(animacoes)

animacoes.sort(key=lambda x: len(x)) # Ordena por tamanho de dígitos ou caracteres
print(animacoes)

animacoes.sort(key=lambda x: len(x), reverse=True) # Primeiro ele ordena por tamanho
# de dígitos ou caracteres, depois ele inverte a lista ao contrário
print(animacoes)

#--------------------------------------------------------------------------------------------------------

# len(): verifica o tamanho da lista, ou seja, a quantidade de elementos que ela possui.

print(len(animacoes))

#--------------------------------------------------------------------------------------------------------

# sorted(): parecido com o sort()

print(linguagens)

print(sorted(linguagens))

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))
