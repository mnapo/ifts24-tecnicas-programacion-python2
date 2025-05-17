# pedir cantidad de segundos e indicar cuantos minutos y segundos son
import math
segundos = 0
minutos = 0
while True:
  try:
    segundos = int(input("Ingrese cantidad de segundos:"))
    break
  except ValueError:
    print("Cantidad inválida")
    continue
minutos = math.floor(segundos/60)
segundos = segundos - minutos * 60
print("Minutos: ", minutos)
print("Segundos: ", segundos)
