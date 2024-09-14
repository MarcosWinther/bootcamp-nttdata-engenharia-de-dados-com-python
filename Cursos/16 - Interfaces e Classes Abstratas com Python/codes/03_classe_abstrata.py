from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    # Antigamente por ser property era @abstractproperty, mas já está depreciado
    # Agora é @abstract method também
    @property
    @abstractmethod 
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")
    
    @property
    def marca(self):
        return "SAMSUNG"

class ControleSom(ControleRemoto):
    def ligar(self):
        print("Ligando o som...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o som...")
        print("Desligado!")
    
    @property
    def marca(self):
        return "LG"


controle_tv = ControleTv()

print(controle_tv.marca)
controle_tv.ligar()
controle_tv.desligar()

controle_som = ControleSom()

print(controle_som.marca)
controle_som.ligar()
controle_som.desligar()