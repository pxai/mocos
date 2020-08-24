import listado
miListado = listado.Listado("4.json")

if miListado.existe("eugene"):
    print("Existe!")

miListado.aMinusculas()
miListado.print()

if miListado.existe("eugene"):
    print("Existe!")
    print(miListado.posicion('eugene'))
