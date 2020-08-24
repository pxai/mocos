import random

def aleatorio (max):
    return random.randint(0, max)

class Dado:
    def __init__(self, lados = 6, admiteCero = False):
        self._lados = lados
        self._admiteCero = admiteCero

    @property
    def lados (self):
        return self._lados

    @lados.setter
    def lados (self, lados):
        self._lados = lados

    @property
    def admiteCero (self):
        return self._admiteCero

    @admiteCero.setter
    def admiteCero (self, admiteCero):
        self._admiteCero = admiteCero

    def tirar (self):
        numero =  aleatorio(self._lados)

        if not self._admiteCero:
            numero = numero + 1

        return numero



dado = Dado()
for i in range(10):
    print(dado.tirar())
