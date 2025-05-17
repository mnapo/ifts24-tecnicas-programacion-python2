# función para decidir si una cadena es palíndromo
import math

def inversa(cadena):
  temp = ""
  for i in range(len(cadena)-1, -1, -1):
    temp+=cadena[i]
  return temp

def es_palindromo(cadena):
  temp = inversa(cadena)
  print(temp)
  if (cadena==temp):
    return True
  else:
    return False

"""
Optimizado para cadenas largas (invertir solo la segunda mitad)

def es_palindromo(cadena):
  temp1 = ""
  temp2 = ""
  longitud = len(cadena)
  if (longitud%2==0):
    media_longitud = int(longitud/2)
    temp2 = cadena[media_longitud:longitud]
  else:
    media_longitud = int(math.floor(longitud/2))
    temp2 = cadena[media_longitud+1:longitud]
  temp1 = cadena[0:media_longitud]
  temp2 = inversa(temp2)
  if (temp1==temp2):
    print("allboys")
    return True
  return False
"""
