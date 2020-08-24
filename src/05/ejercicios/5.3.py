class Vehiculo:
    def __init__(self, matricula):
        self._matricula = matricula

    @property
    def matricula (self):
        return self._matricula

    @matricula.setter
    def matricula (self, matricula):
        self._matricula = matricula

    def arrancar (self):
        print("Arrancando ", self._matricula)


class Coche(Vehiculo):
    def __init__(self, matricula, modelo, color):
        super().__init__(matricula)
        self._modelo = modelo
        self._color = color

    def info (self):
        return f"{self.matricula} {self._modelo} {self._color}";


coche = Coche("0042ASI", "Opel Corsa", "Blanco")
coche.arrancar()
print(coche.info())
