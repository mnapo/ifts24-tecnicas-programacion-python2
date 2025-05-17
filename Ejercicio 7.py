# calcular distancia
horas = 0
velocidad = 0
distancia = 0
while True:
  try:
    horas = int(input("Ingrese la cantidad de horas:"))
    break
  except ValueError:
    print("Cantidad inválida")
while True:
  try:
    velocidad = int(input("Ingrese la velocidad:"))
    break
  except ValueError:
    print("Cantidad inválida")
    continue
distancia = horas * velocidad
print("Distancia: ", distancia)
