class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    # para setar o valor, usamos @--.setter
    # Atenção: não posso trabalhar esse atributo como método
    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = -1
    
foo = Foo(20)
print(foo.x)

# agora posso setar o valor para somar
foo.x = 20
print(foo.x)

del foo.x
print(foo.x)