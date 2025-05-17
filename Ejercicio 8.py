# calcular distancia
import math
nota = 0
suma_notas = 0
for i in range(7):
  while nota==0:
    try:
      nota = int(input("Ingrese la nota:"))
    except ValueError:
      print("Nota inválida")
      continue
    if nota<0 or nota>10:
      nota = 0
      print("Nota inválida")
    suma_notas += nota
  nota = 0
print("Promedio: ", math.floor(suma_notas/7))
