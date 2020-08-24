import json

class Listado:
    def __init__ (self, nombreFichero):
        contenido = open(nombreFichero, "r")
        self._datos = json.load(contenido)
        contenido.close()

    def existe (self, nombre):
        for dato in self._datos:
            if dato["nombre"] == nombre:
                return True

        return False

    def aMinusculas (self):
        self._datos = list(map(lambda dato: { "id": dato["id"], "nombre": dato["nombre"].lower() }, self._datos))

    def posicion (self, nombre):
        i = 0
        for dato in self._datos:
            if dato["nombre"] == nombre:
                return i
            i += 1
        return -1

    def print (self):
        for dato in self._datos:
            print(dato)
