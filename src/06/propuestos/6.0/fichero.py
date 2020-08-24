class Fichero:
    def __init__ (self, nombreFichero):
        self._nombreFichero = nombreFichero

    def leer (self):
        fichero = open(self._nombreFichero, "r")
        datos = fichero.read()
        fichero.close()

        return datos

    def escribir (self, contenido):
        fichero = open(self._nombreFichero, "w+")
        fichero.write(contenido)
        fichero.close()
