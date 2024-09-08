salario = 3000

# Função sobrecarregada de tarefas
# Essa função não é uma boa prática
# Essa função é só mesmo para aplicar o conceito visto em aula
def mudar_lista_e_calcular_salario_bonus(bonus, lista):
    global salario

    # lista.append(2) - dará problema
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista auxiliar={lista_aux}")

    salario += bonus
    return salario

lista = [2]
print(lista)

salario_com_bonus_mais_lista = mudar_lista_e_calcular_salario_bonus(1000, lista)
print(salario_com_bonus_mais_lista)