# pedir horas trabajadas y costo por hora y mostrar pago
horas_trabajadas = 0
costo_hora = 0
pago = 0
while True:
  try:
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas:"))
    break
  except ValueError:
    print("Cantidad inválida")
while True:
  try:
    costo_hora = int(input("Ingrese el costo por hora:"))
    break
  except ValueError:
    print("Cantidad inválida")
    continue
pago = horas_trabajadas * costo_hora
print("Pago: ", pago)
