codigo = ""
total = 150
dias = 0
id_categoria = 0
categoria_existente = False
categorias = [
    {"codigo":"nacl", "descripcion":"nacional", "recargo_dia":10.5},
    {"codigo":"intl", "descripcion":"internacional", "recargo_dia":30.25},
    {"codigo":"naes", "descripcion":"nacional estreno", "recargo_dia":50.8},
    {"codigo":"ines", "descripcion":"internacional estreno", "recargo_dia":100.62}
]

while categoria_existente == False:
  try:
    codigo = input("Ingrese el código de categoría:")
    for i in range(0, len(categorias)):
      if (codigo==categorias[i]["codigo"]):
        categoria_existente = True
        id_categoria = i
  except ValueError:
    print("Código inválido")
    continue

while True:
  try:
    dias = int(input("Ingrese días de atraso:"))
  except ValueError:
    print("Cantidad de días inválida")
    continue
  break

total+=categorias[id_categoria]["recargo_dia"]*dias
print("Total: ", total)
