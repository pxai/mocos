function aleatorio (max):
    return Math.round(Math.random() * max)


class Dado:
    def __init__(self, lados = 6, admiteCero = False):
        self._lados = lados
        self._admiteCero = admiteCero


    def set lados (self, lados):
        self._lados = lados


    def set admiteCero (self, admiteCero):
        self._admiteCero = admiteCero


    def tirar (self):
        numero =  aleatorio(self._lados)

        if not self._admiteCero:
            numero = numero + 1

        return numero



dado = Dado()
