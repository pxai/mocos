import tareas
misTareas = tareas.Tareas()

print(misTareas.mostrar(), "\n---")

misTareas.crear(2, "Comer")
print(misTareas.mostrar(), "\n---")

misTareas.eliminar(2)
print(misTareas.mostrar(), "\n---")

misTareas.crear(66, "Leer")
print(misTareas.mostrar(), "\n---")
misTareas.guardar()
