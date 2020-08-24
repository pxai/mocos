class Comida:
    def __init__(self, nombre):
        self.nombre = nombre


class Fruta(Comida):
    def __init__(self, nombre, vitaminas):
        super().__init__(nombre)
        self.vitaminas = vitaminas

    def info (self):
        # return f"{self.nombre} {self.vitaminas}";
        return self.nombre + " " + str(self.vitaminas)

postre = Fruta("Kiwi", ["A", "C"])
print(postre.info())
