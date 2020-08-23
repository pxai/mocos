fichero = open("texto.txt", "r")
lineas = fichero.readline()
for linea in lineas:
    print(linea)

fichero.close()