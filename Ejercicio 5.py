# pedir temperatura en celcius y escribirla en fahrenheit
import math
celsius = 0
fahrenheit = 0
while True:
  try:
    celsius = int(input("Ingrese grados celsius:"))
    break
  except ValueError:
    print("Cantidad inválida")
    continue
fahrenheit = celsius * 1.8 + 32
print("Grados Fahrenheit: ", fahrenheit)
