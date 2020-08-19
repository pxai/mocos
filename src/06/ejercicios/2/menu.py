class Menu:
    def __init__ (self, opciones):
        self._opciones = opciones

    def mostrar (self):
        for i in range(len(self._opciones)):
            print(f"{i+1} {self._opciones[i]}")

    def seleccionar (self, numero):
        return numero > 0 and numero <= len(self._opciones)
