telefonos = {"Ada": 666555333, "Bug": 111000111 }

nombre = input("Introduce un nombre: ")

del telefonos[nombre]

for nombre in telefonos.keys():
    print(nombre, telefonos[nombre])

