class NombreFormateado:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def formatear (self):
        return self._corregir(self._nombre) + " " + self._corregir(self._apellido)


    def _corregir (self, cadena):
        return self._primero(cadena) + self._resto(cadena)


    def _primero (self, cadena):
        return cadena[0].upper()


    def _resto (self, cadena):
        return cadena[1:len(cadena)].lower()


formateador = NombreFormateado("JUAN", "PÉREZ")
print(formateador.formatear())
