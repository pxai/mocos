from datetime import date

import fichero

miFichero = fichero.Fichero("6.0.txt")

print("Contenido anterior: ", miFichero.leer())

miFichero.escribir("Contenido cambiado!!! " + str(date.today()))
print("Conten", miFichero.leer())
