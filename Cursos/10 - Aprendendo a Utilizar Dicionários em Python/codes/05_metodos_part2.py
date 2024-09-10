contatos = {
    "winthermarcos@gmail.com": {"nome": "Marcos", "telefone": "64 9 9876-5432"},
    "thaissilva@gmail.com": {"nome": "Thais Silva", "telefone": "64 9 9123-4567"},
    "celiaaparecida@gmail.com": {"nome": "Celia Aparecida", "telefone": "62 9 9216-9874"},
}

print(contatos)

#------------------------------------------------------------------------------------------------------

# update()

contatos.update({"winthermarcos@gmail.com": {"nome": "Marcos W"}})
print(contatos)

contatos.update({"winthermarcos@gmail.com": {"nome": "Marcos Winther", "telefone": "64 9 9876-5432"}})
print(contatos)

#------------------------------------------------------------------------------------------------------

# values
## Retorna somente os valores

print(contatos.values())

#------------------------------------------------------------------------------------------------------

# in

resultado = "winthermarcos@gmail.com" in contatos
print(resultado)

resultado = "marcoswinther@dev.com" in contatos
print(resultado)

resultado = "idade" in contatos["winthermarcos@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["winthermarcos@gmail.com"]
print(resultado)

#------------------------------------------------------------------------------------------------------

# del

del contatos["winthermarcos@gmail.com"]["telefone"]
print(contatos)

del contatos["thaissilva@gmail.com"]
print(contatos)