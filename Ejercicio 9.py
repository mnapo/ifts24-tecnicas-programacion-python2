# calcular capital obtenido de la inversión
inversion = 0
interes_anual = 0
años = 0
capital_obtenido = 0
while True:
  try:
    inversion = float(input("Ingrese cantidad a invertir:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
while True:
  try:
    interes_anual = float(input("Ingrese interés anual:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
while True:
  try:
    años = int(input("Ingrese cantidad de años:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
capital_obtenido = inversion*interes_anual/100*años
print("Capital obtenido: ", capital_obtenido)
