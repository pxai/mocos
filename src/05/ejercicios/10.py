class Jugador:
    def __init__(self, nombre, posicion, dorsal):
        self._nombre = nombre
        self._posicion = posicion
        self._dorsal = dorsal

    def informe (self):
        return f"{self._nombre} {self._posicion} {self._dorsal}"


class Equipo:
    def __init__ (self, nombre, fundacion, presupuesto):
        self._nombre = nombre
        self._fundacion = fundacion
        self._presupuesto = presupuesto
        self._jugadores = []

    def ficharJugador (self, jugador):
        self._jugadores.append(jugador)

    def mostrarJugadores (self):
        for jugador in self._jugadores:
            print(jugador.informe())


jugador1 = Jugador("Maradona", "Delantero", 10)
jugador2 = Jugador("Beckenbauer", "Defensa", 4)

print(jugador1.informe())

equipo = Equipo("New Team", 1983, 39944.45)
equipo.ficharJugador(jugador1)
equipo.ficharJugador(jugador2)

equipo.mostrarJugadores()
