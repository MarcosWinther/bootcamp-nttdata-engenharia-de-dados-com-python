# Métodos matemáticos

## union()

conjunto_a = {10, 20, 30, 40}
conjunto_b = {50, 60, 70, 80}

print(conjunto_a.union(conjunto_b))

#-----------------------------------------------------------------------------

## intersection()

conjunto_c = {100, 200, 300, 400}
conjunto_d = {400, 200, 500, 600}

print(conjunto_c.intersection(conjunto_d))

#-----------------------------------------------------------------------------

## difference()

print(conjunto_c.difference(conjunto_d))
print(conjunto_d.difference(conjunto_c))

#-----------------------------------------------------------------------------

## symmetric_difference()

print(conjunto_c.symmetric_difference(conjunto_d))

#-----------------------------------------------------------------------------

## issubset()

conjunto_e = {1, 2, 3, 4}
conjunto_f = {7, 8, 4, 3, 2, 1}

print(conjunto_e.issubset(conjunto_f))
print(conjunto_f.issubset(conjunto_e))

#-----------------------------------------------------------------------------

## issuperset()

print(conjunto_e.issuperset(conjunto_f))
print(conjunto_f.issuperset(conjunto_e))

#-----------------------------------------------------------------------------

## isdisjoint()

print(conjunto_e.isdisjoint(conjunto_f))
print(conjunto_f.isdisjoint(conjunto_c))

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


# Outros métodos

## add()

sorteio = {24, 48}

sorteio.add(12)
sorteio.add(36)
sorteio.add(12) # como já existe, será ignorado

print(sorteio)

#-----------------------------------------------------------------------------

## clear()

sorteio.clear() # limpa todo o set

print(sorteio)

#-----------------------------------------------------------------------------

## copy()

sorteio_2 = {4, 8, 16, 20}
sorteio_3 = sorteio_2.copy()

print(sorteio_2)
print(sorteio_3)

#-----------------------------------------------------------------------------

## discard()

numeros = {1, 2, 4, 6, 8, 10, 1}

print(numeros)

numeros.discard(1)
numeros.discard(3)

print(numeros)

#-----------------------------------------------------------------------------

## pop(): aqui no set o pop retira o primeiro valor

numeros.pop()
print(numeros)

numeros.pop()
print(numeros)

#-----------------------------------------------------------------------------

## remove()

# parecido com o discard()
# mas se tentar remover um valor que não existe, o programa dará erro.

# se eu tentasse numeros.remove(7) vai apresentar erro

# Abaixo um exemplo que dará certo
numeros.remove(6)

#-----------------------------------------------------------------------------

## len()

print(len(numeros))

#-----------------------------------------------------------------------------

## in: verifica se um elemento está em um determinado conjunto

numeros_pares = {2, 4, 6, 8, 10, 12, 14}

print(1 in numeros)
print(8 in numeros_pares)