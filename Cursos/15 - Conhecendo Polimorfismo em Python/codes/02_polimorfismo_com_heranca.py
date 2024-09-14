class Passaro:
    def voar(self):
        print("Esse pássaro voa!")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("O avestruz não voa!")

def plano_voo(obj):
    obj.voar()

pardal = Pardal()
avestruz = Avestruz()

# Posso chamar com a classe ou com a variável instanciando a classe
plano_voo(Pardal())
plano_voo(Avestruz())