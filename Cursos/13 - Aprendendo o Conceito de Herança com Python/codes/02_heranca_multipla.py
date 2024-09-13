class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return 'Classe Mamífero'

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return "Classe Ave"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class FalarMixin():
    def falar(self):
        return "Hello World!"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        # print(Ornitorrinco.__mro__) # Ordem da resolução que o Python encontra os atributos
        print(Ornitorrinco.mro()) # Ordem da resolução que o Python encontra os atributos
        super().__init__(nro_patas=nro_patas, cor_pelo=cor_pelo, cor_bico=cor_bico)

    def __str__(self):
        return 'Ornitorrinco'

# gato = Gato(nro_patas=4, cor_pelo="Laranja")
# print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Marrom", cor_bico="Preto")
print(ornitorrinco)

print(ornitorrinco.falar())