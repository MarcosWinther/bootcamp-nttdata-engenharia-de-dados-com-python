# Position Only (por posição)

def detalhar_filmes_animacoes(nome, studio, /, ano):
    print(f"Filme: {nome}, foi produzido pelos Estúdios {studio} e lançado em {ano}.")

# Antes da barra é os parâmentros são obrigatórios ser passados por posição nessa função
detalhar_filmes_animacoes("Mulan", "Disney", 1998) # Válido

# Depois da barra, nessa função, é opcional o parâmetro ser passado por nome
detalhar_filmes_animacoes("Rei Leão", "Disney", ano=1994) # Válido

#-------------------------------

# Keyword only (por nome)

def detalhar_series(*, nome, plataforma, numero_temporada, ano):
    print(f"A série {nome} está disponível na plataforma {plataforma}, " +
          f"com {numero_temporada} temporadas lançadas e com seu último lançamento em {ano}.")

# Se não passarmos os nomes dos parâmetros, a função se tornará inválida, pois os nomes são obrigatórios
# Exemplo de formato válido:
detalhar_series(nome="Heartstopper", plataforma="Netflix", numero_temporada=3, ano=2024) # Válido

#-----------------------------------

# Keyword and position only (por nome e posição)

# Antes da /: os parâmetros são passados por posição
# Depois do *: os parâmetros são passados por nome
def detalhar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

detalhar_carro("Palio", 1999, "SAC-854", marca="Fiat", motor=1.0, combustivel="Gasolina")