class Comida:
    def __init__(self,nombre, peso):
        self._nombre = nombre
        self._peso = peso

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    @property
    def peso (self):
        return self._peso

    @peso.setter
    def peso (self, peso):
        self._peso = peso

    def toString (self):
        return f"{self._nombre} {self._peso}"


class Fruta extends Comida:
    def __init__(selfnombre, peso, vitamina):
        super().__init__(nombre, peso)
        self._vitamina = vitamina

    @property
    def vitamina (self):
        return self._vitamina

    @vitamina.setter
    def vitamina (self, vitamina):
        self._vitamina = vitamina

    toString (self):
        return f"{super().toString()} {self._vitamina}"


class Caramelo extends Comida:
    def __init__(selfnombre, peso, calorias):
        super(nombre, peso)
        self._calorias = calorias

    @property
    def calorias (self):
        return self._calorias

    @calorias.setter
    def calorias (self, alorias):
        self._calorias = calorias

    def toString (self):
        return f"{super().toString()} {self._calorias}"


class Cesta:
    def __init__(self):
        self._alimentos = []

    def meterComida (self, comida):
        self._alimentos.append(comida)

    def pesoTotal (self):
        total = 0
        for alimento in self._alimentos::
            total += self._alimentos[i].peso

        return total

    def toString (self):
        info = ""
        for alimento in self._alimentos:
            info = info + self._alimentos[i] + "\n"

        return info


chicle = Caramelo("Cheiw", 0.2, 100)
gominola = Caramelo("Fresa", 0.3, 210)
pera = Fruta("Pera", 0.1, "B")
manzana = Fruta("Manzana", 0.15, "A")

cesta = Cesta()
cesta.meterComida(chicle)
cesta.meterComida(gominola)
cesta.meterComida(pera)
cesta.meterComida(manzana)

print("Contenido cesta: ", cesta.toString())
print("Peso total:", cesta.pesoTotal())
