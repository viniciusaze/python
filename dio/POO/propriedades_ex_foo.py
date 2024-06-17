class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # Transforma metodo em propriedade/atributo
    def x(self):
        return self._x or 0
    
    @x.setter # Modificando o x
    def x(self, value):
        # return self._x + value Sintaxe errada, pois agora ele não é um metodo e sim um atributo
        # Abaixo a sintaxe certa, trabalhando como atributo
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0
    

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)