class Instrumento:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo

    def tocar (self):
        print("Tocando ", self._nombre)

    def info (self):
        return f"{self._nombre} {self._tipo}"


miGuitarra = Instrumento("Guitarra", "cuerda")
miGuitarra.tocar()
print(miGuitarra.info())
