contatos = {
    "winthermarcos@gmail.com": {"nome": "Marcos Winther", "telefone": "64 9 9876-5432"},
    "thaissilva@gmail.com": {"nome": "Thais Silva", "telefone": "64 9 9123-4567"},
    "celiaaparecida@gmail.com": {"nome": "Celia Aparecida", "telefone": "62 9 9216-9874"},
}

## -----------------------------------------------------------------------------------------

# clear()

contatos.clear()

print(contatos)

## -----------------------------------------------------------------------------------------

contatos = {
    "winthermarcos@gmail.com": {"nome": "Marcos Winther", "telefone": "64 9 9876-5432"},
    "thaissilva@gmail.com": {"nome": "Thais Silva", "telefone": "64 9 9123-4567"},
    "celiaaparecida@gmail.com": {"nome": "Celia Aparecida", "telefone": "62 9 9216-9874"},
}

## -----------------------------------------------------------------------------------------

# copy()

copia = contatos.copy()

copia["winthermarcos@gmail.com"] = {"nome": "Marcos"}

print(copia)

#-------------------------------------------------------------------------------------------

# fromkeys()
## Permite criar o dicionário com valor vazio ou padrão

cantoras = dict.fromkeys(["nome", "genero_musical"])
print(cantoras)

cantores = dict.fromkeys(["nome", "genero_musical"], "vazio")
print(cantores)

#-------------------------------------------------------------------------------------------

# get()
## Outra forma de acessar valores dentro do dicionário

## Se você informar uma chave que não existe
## O get retornará None
print(contatos.get("idade"))
print(contatos.get("idade", {}))

## Testando com chaves existentes no dicionário contatos
print(contatos.get("winthermarcos@gmail.com"))
print(contatos.get("winthermarcos@gmail.com", {}))

#-------------------------------------------------------------------------------------------

# items()
### Devolve uma lista de tuplas

print(contatos.items())

#-------------------------------------------------------------------------------------------

# keys()
## Retorna só as chaves do dicionário
## Muito útil para saber quantas e quais chaves seu dicionário tem

print(contatos.keys())

#-------------------------------------------------------------------------------------------

# pop()
## Apaga a chave solicitada com seus respectivos valores
## Caso você informa uma chave que não existe, você pode informar a ele devolver uma {} vazia

resultado = contatos.pop("winthermarcos@gmail.com")
print(resultado)

resultado = contatos.pop("winthermarcos@gmail.com", {})
print(resultado)

#-------------------------------------------------------------------------------------------

# popitem()
## Se não tiver mais chaves, o programa retorna um erro

contatos.popitem()
print(contatos)

#-------------------------------------------------------------------------------------------

# setdefault()
## Adiciona o valor e a chave caso a chave não exista

contato = {"nome": "Marcos Winther", "email": "winthermarcos@gmail.com"}

## Como a chave email já existe, o valor não será adicionado no dicionário
contato.setdefault("email", "thais.carreiro@gmail.com")
print(contato)

## Como não existe no dicionário, será adicionada a chave idade e o seu valor no dicionário.
contato.setdefault("idade", 28)
print(contato)

