import json
import jugador

class Equipo:
    def cargar (self):
        contenido = open("./jugadores.json")
        jugadores = json.load(contenido)
        print("Loaded: ", jugadores)
        self._jugadores = []
        for j in jugadores:
            self._jugadores.append(jugador.Jugador(j["nombre"], j["dorsal"]))

    def fichaje (self, nombre, dorsal):
        nuevoFichaje = jugador.Jugador(nombre, dorsal)
        self._jugadores.append(nuevoFichaje)

    def mostrar (self):
        for jugador in self._jugadores:
            print(jugador.toString())
