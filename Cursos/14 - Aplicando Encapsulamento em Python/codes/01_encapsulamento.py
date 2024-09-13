class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
          
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    
conta = Conta("0001", 100.00)

# Errado
# Funciona, mas não é recomendado
# print(conta._saldo) ## Esse tipo de acesso nós programadores não fazemos

# Esse é permitido
print(conta.nro_agencia)

# Esse também é permitido
print(conta.mostrar_saldo())