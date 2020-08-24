telefonos = {"Ada": 666555333, "Bug": 111000111 }

nombre = input("Introduce un nombre: ")
telefono = input("Introduce un número: ")

telefonos[nombre] = int(telefono)

for nombre in telefonos.keys():
    print(nombre, telefonos[nombre])

