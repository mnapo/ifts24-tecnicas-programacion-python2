# calcular peso paquete
payasos = 0
muñecas = 0
peso = 0
while True:
  try:
    payasos = int(input("Ingrese cantidad de payasos:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
while True:
  try:
    muñecas = int(input("Ingrese cantidad de muñecas:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
peso = payasos*11.2+muñecas*7-5
print("Peso por paquete: ", peso)
