# pedir pies y pulgadas y convertir a cm
import math
pies = 0
pulgadas = 0
cm = 0
while True:
  try:
    pies = int(input("Ingrese pies:"))
    break
  except ValueError:
    print("Cantidad inválida")
    continue
while True:
  try:
    pulgadas = int(input("Ingrese pulgadas:"))
    break
  except ValueError:
    print("Cantidad inválida")
    continue
pulgadas += pies * 12
cm = pulgadas * 2.54
print("Centímetros: ", cm)
