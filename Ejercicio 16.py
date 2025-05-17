# convertir a mayúscula la primer letra de cada palabra

def mayusculas(texto):
  palabras = texto.split()
  palabras_con_mayuscula = []
  texto = " "
  for i in range(0, len(palabras)):
    primera_letra = palabras[i][0].upper()
    resto_palabra = palabras[i][1:len(palabras[i])]
    palabras_con_mayuscula.append(primera_letra+resto_palabra)
  return texto.join(palabras_con_mayuscula)
