peso = input("Introduce tu peso: ")
altura = input("Introduce tu altura: ")
peso = int(peso)
altura = int(altura)

imc = peso / (altura * altura)

imcRedondeado = (imc * 10000)
print("Tu imc: ", imcRedondeado)

if imcRedondeado < 16 :
  print("Necesitas comer más")
elif imcRedondeado >= 16 and imcRedondeado < 25:
  print("Estás bien")
elif imcRedondeado >= 25 and imcRedondeado < 30:
  print("Tienes sobrepeso")
else:
  print("Tienes un problema de obesidad")
