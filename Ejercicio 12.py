'''
Se pide obtener que tipo de triángulo es.
Sabiendo que ingresan 3 datos correspondientes al largo de cada lado.
Recordar: el triángulo equilátero tiene los 3 lados iguales, el isósceles 2 lados iguales y el escaleno los 3 lados distintos.
'''

def tipo_triangulo(lado1, lado2, lado3):
  if lado1==lado2 and lado2==lado3:
    return "equilátero"
  elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    return "isóceles"
  else:
    return "escaleno"

def ingresar_lado():
  lado = 0
  while True:
    try:
      lado=float(input("Ingrese la medida del lado:"))
      if lado<=0:
        print("La medida del lado debe ser positiva, reingresar")
        continue
    except ValueError:
      print("La medida del lado es incorrecta, reingresar")
      continue
    return lado

lado1 = ingresar_lado()
lado2 = ingresar_lado()
lado3 = ingresar_lado()
print("El triángulo es", tipo_triangulo(lado1, lado2, lado3))
