class Sumador:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    @property
    def valor1 (self):
        return self._valor1

    @valor1.setter
    def valor1 (self, valor1):
        if valor1 > 0:
            self._valor1 = valor1
        else:
            self._valor1 = 0

    @property
    def valor2 (self):
        return self._valor2

    @valor2.setter
    def valor2 (self, valor2):
        if valor2 > 0:
            self._valor2 = valor2
        else:
            self._valor2 = 0

    def sumar (self):
        return self._valor1 + self._valor2


sumador = Sumador(28, 14)
print(sumador.sumar())

sumador.valor1 = 600
sumador.valor2 = 66
print(sumador.sumar())
