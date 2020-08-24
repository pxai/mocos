numero1 = input("Introduce un número: ")
numero2 = input("Introduce otro número: ")

resto = int(numero1) % int(numero2)

if resto == 0:
  print(numero1, " es múltiplo de ", numero2)
else:
  print(numero1, " NO es múltiplo de ", numero2)
