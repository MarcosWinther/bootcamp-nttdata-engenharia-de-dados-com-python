# Operador AND
print(True and True)
print(True and False)
print(False and False)

# Operador OR
print(True or True)
print(True or False)
print(False or False)

# expressão
valor_1 = 2000
valor_2 = 400
valor_3 = 400
valor_booleano = True

exp = valor_1 >= valor_2 and valor_2 <= valor_3 or valor_booleano and valor_1 >= valor_2
print(exp)

exp_2 = (valor_1 >= valor_2 and valor_2 <= valor_3) or (valor_booleano and valor_1 >= valor_2)
print(exp_2)