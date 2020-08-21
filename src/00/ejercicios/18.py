edades = {"Ada": 14, "Bug": 10, "Neko": 2}

print(edades) 

edades["Miranda"] = 23;

print(edades) # ["Ada", "Bug", "Neko", "Miranda"]

del edades["Bug"]

print(edades) # ["Ada", "Neko", "Miranda"]

for nombre in edades.keys():
    print(nombre, edades[nombre])

