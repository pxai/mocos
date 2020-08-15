class Dispositivo:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre ():
        return self._nombre

    def set_nombre (nombre):
        self._nombre = nombre

    def get_precio ():
        return self._precio

    def set_precio (precio):
        self._precio = precio

    def toString (self):
        return f"{self._nombre} {self._precio}";


class Movil(Dispositivo):
    def __init__(self, nombre, precio, numero):
        super().__init__(nombre, precio)
        self._numero = numero

    @property
    def numero (self):
        return self._numero

    @numero.setter
    def numero (self, numero):
        self._numero = numero

    def toString ():
        return f"{super().toString()} {self._numero}"

    def llamar (numero):
        print("Llamando a", numero)


class Ordenador(Dispositivo):
    def __init__(self, nombre, precio, procesador):
        super().__init__(nombre, precio)
        self._procesador = procesador

    @property
    def procesador (self):
        return self._procesador

    @procesador.setter
    def procesador (self, procesador):
        self._procesador = procesador

    def toString (self):
        return f"{super().toString()} {self._procesador}"


ordenador = Ordenador("Dell", 4553.4, "Lentium 4")
telefono = Movil("Chanmhung", 434.4, 665745345)

print("Ordenador: ", ordenador)
print("Telefono: ", telefono.toString())
