nome = "mArCoS WinTHer"

# upper: converte todos os caracteres para maiúsculo
print(nome.upper())

# lower: convrte todos os caracteres para minúsculo
print(nome.lower())

# title: título
print(nome.title())

#---------------------

# Eliminando espaços em branco

frase = " Hello World! "

# strip: elimina o espaço tanto da direita quando da esquerda
print(frase.strip())

# lstrip: elimina espaço da esquerda
print(frase.lstrip())

# rstrip: elimina espaço da direita
print(frase.rstrip())

#-------------------------

curso = "Python"

# Junções e centralizações

print(curso.center(10, "#"))

print(".".join(curso))

# Comparando join com for

for letra in curso:
    print(letra, end="-")