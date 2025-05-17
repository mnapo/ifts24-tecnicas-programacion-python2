# calcular monto total

productos = []

def obtener_precio(productos, codigo):
  for i in range(0, len(productos)):
    if productos[i]["codigo"] == codigo:
      return productos[i]["precio"]
  return 0

def agregar_producto(lista_productos, codigo, nombre, precio):
  producto = {"codigo":codigo, "nombre":nombre, "precio":precio}
  return lista_productos.append(producto)

def obtener_subtotal(productos):
  codigo = ""
  precio = 0
  cantidad = 0
  subtotal = 0

  while precio==0:
    codigo = str(input("Ingrese el código de producto:"))
    precio = obtener_precio(productos, codigo)
  while True:
    try:
      cantidad = int(input("Ingrese la cantidad a comprar:"))
    except ValueError:
      print("Cantidad inválida")
      continue
    break

  subtotal = cantidad * precio
  print("Subtotal: ", subtotal)
  

agregar_producto(productos, "SMGA04", "Celular Samsung A04", 2100000.50)
agregar_producto(productos, "SMGA32", "Celular Samsung A32", 4506128.00)
agregar_producto(productos, "IPH7", "Celular Iphone 7", 180000000.00)
agregar_producto(productos, "IPH10", "Celular Iphone 10", 350000000.80)
agregar_producto(productos, "MSE_4", "Mouse Modelo 4", 2500.75)
agregar_producto(productos, "MSE_8", "Mouse Modelo 8", 3706.89)

while True:
  obtener_subtotal(productos)
