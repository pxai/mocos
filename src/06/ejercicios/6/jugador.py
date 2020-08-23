class Jugador:
    def __init__ (self, nombre, dorsal):
        self._nombre = nombre
        self._dorsal = dorsal

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    @property
    def dorsal (self):
        return self._dorsal

    @dorsal.setter
    def dorsal (self, dorsal):
        self._dorsal = dorsal

    def toString (self):
        return self._nombre + " " + str(self._dorsal)
