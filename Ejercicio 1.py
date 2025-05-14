# Ingresar 10 letras y determinar si son vocales o consonantes

vocales = ["a", "e", "i", "o", "u"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letras_ingresadas = 0
while letras_ingresadas<10:
  letra = str(input("Ingrese una letra:")).lower()
  if letra in vocales:
    print("La letra es una vocal")
    letras_ingresadas+=1
  elif letra in consonantes:
    print("La letra es una consonante")
    letras_ingresadas+=1
  else:
    print("No ingreso una letra válida, reingresar")
