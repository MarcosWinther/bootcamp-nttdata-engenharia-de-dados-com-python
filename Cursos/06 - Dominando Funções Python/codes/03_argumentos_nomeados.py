def detalhar_animacoes(nome, studio, ano):
    print(f"A animação '{nome}' é produzida pelo Estúdio {studio} e foi lançada no ano de {ano}.")

detalhar_animacoes("Divertidamente 2", "Disney", 2024)

## Utilizando argumentos nomeados nessa chamada de função
detalhar_animacoes(nome="O Rei Leão", studio="Disney", ano=1994)

## Utilizando argumentos nomeados com dicionário nessa nova chamada de função
detalhar_animacoes(**{"nome": "Mulan", "studio": "Disney", "ano": 1998})