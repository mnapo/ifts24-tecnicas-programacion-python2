# decidir si dos palabras riman

def riman(palabra1, palabra2):
  if (len(palabra1)>=3 and len(palabra2)>=3):
    if (palabra1[-3]==palabra2[-3]):
      return "las palabras riman"
    elif (palabra1[-2]==palabra2[-2]):
      return "las palabras riman un poco"
    else:
      return "las palabras no riman"
  else:
    return "las palabras son muy cortas"

print(riman("pipón", "tendón"))
print(riman("la", "me"))
print(riman("cavernícola", "agrícola"))
print(riman("mequetrefe", "libro"))
