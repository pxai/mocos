import json

fichero = open("texto.json", "r")
contenido = json.load(fichero)
fichero.close()

personaje = { "id": 666, "nombre": "Gumball" }
contenido.append(personaje)

fichero = open("texto.json", "w")
fichero.write(json.dumps(contenido))
fichero.close()