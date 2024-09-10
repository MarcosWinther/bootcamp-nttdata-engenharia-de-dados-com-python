contatos = {
    "winthermarcos@gmail.com": {"nome": "Marcos Winther", "telefone": "64 9 9876-5432"},
    "thaissilva@gmail.com": {"nome": "Thais Silva", "telefone": "64 9 9123-4567"},
    "celiaaparecida@gmail.com": {"nome": "Celia Aparecida", "telefone": "62 9 9216-9874"},
}

# Funciona, mas não é a melhor forma
for chave in contatos:
    print(chave, contatos[chave])

# Essa é a melhor forma
for chave, valor in contatos.items():
    print(chave, valor)