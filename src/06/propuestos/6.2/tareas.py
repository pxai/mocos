import json

class Tareas:
    def __init__ (self):
        fichero = open("tareas.json", "r")
        self._tareas = json.load(fichero)
        fichero.close()

    def crear (self, id, tarea):
        nueva = { "id": id, "tarea": tarea };
        self._tareas.append(nueva)

    def guardar (self):
        fichero = open("tareas.json", "w")
        fichero.write(json.dumps(self._tareas))
        fichero.close()

    def eliminar(self, id):
        self._tareas = list(filter(lambda dato: dato["id"] != id, self._tareas))

    def mostrar (self):
        resultado = ""
        for dato in self._tareas:
            resultado += json.dumps(dato) + "\n"

        return resultado
