# calcular puntaje examen
correctas = 0
incorrectas = 0
puntaje = 0
while True:
  try:
    correctas = int(input("Respuestas correctas:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
while True:
  try:
    incorrectas = int(input("Respuestas incorrectas:"))
  except ValueError:
    print("Cantidad inválida")
    continue
  break
puntaje = correctas*4-incorrectas
print("Puntaje obtenido: ", puntaje)
