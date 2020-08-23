import json

fichero = open("texto.json", "r")
contenido = json.load(fichero)

for personaje in contenido:
    print(personaje["nombre"])

fichero.close()