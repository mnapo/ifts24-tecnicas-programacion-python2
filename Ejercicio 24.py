nombre_archivo = ""
palabras = []
cantidad_letras = 0

while True:
    try:
        nombre_archivo = input("Ingrese nombre del archivo:")
    except ValueError:
        print("Nombre de archivo inválido")
        continue
    break

with open(nombre_archivo, "r") as archivo:
    cantidad_letras = len(archivo.read())

print(cantidad_letras)
