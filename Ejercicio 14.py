# función para invertir una cadena

def inversa(cadena):
  temp = ""
  for i in range(len(cadena)-1, -1, -1):
    temp+=cadena[i]
  return temp
