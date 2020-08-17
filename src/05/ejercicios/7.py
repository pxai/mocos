class Piloto:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre



class Aeroplano:
    def __init__(self, modelo, piloto, copiloto):
        self._modelo = modelo
        self._piloto = piloto
        self._copiloto = copiloto

    @property
    def modelo (self):
        return self._modelo

    @modelo.setter
    def modelo (self, modelo):
        self._modelo = modelo

    def volar (self):
        return f"Volando {self._modelo} {self._piloto.nombre} con {self._copiloto.nombre}"


piloto1 = Piloto("Han Solo")
piloto2 = Piloto("Murdock")
avioneta = Aeroplano("AirBluff 727", piloto1, piloto2)

print(avioneta.volar())
