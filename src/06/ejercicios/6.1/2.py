import menu
miMenu = menu.Menu(["Mostrar", "Eliminar", "Salir"])

miMenu.mostrar()

if miMenu.seleccionar(1):
    print("Opción 1 presente")
else:
    print("Opción 1 no presente")
