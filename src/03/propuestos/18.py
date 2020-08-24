edades = {"Ada": 14, "Bug": 10, "Neko": 2}

print(edades)  # {'Bug': 10, 'Neko': 2, 'Ada': 14}

edades["Miranda"] = 23;

print(edades) # {'Bug': 10, 'Neko': 2, 'Ada': 14, 'Miranda': 23}
del edades["Bug"]

print(edades) # {'Neko': 2, 'Ada': 14, 'Miranda': 23}

for nombre in edades.keys():
    print(nombre, edades[nombre])

