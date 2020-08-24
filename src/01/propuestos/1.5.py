dorsal = input("Introduce dorsal: ")
dorsal = int(dorsal)

if dorsal >= 0 and dorsal <= 99:
  if dorsal == 1:
      print("Portero")
  elif dorsal >= 1 and dorsal <= 5:
      print("Defensa")
  elif dorsal >= 6 and dorsal <= 8 or dorsal == 11:
      print("Centrocampista")
  elif dorsal == 9:
      print("Delantero")
  else:
      print("Cualquiera")
else:
    print("Error, el dorsal no está entre 0 y 99")
