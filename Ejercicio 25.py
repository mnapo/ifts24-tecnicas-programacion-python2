nombre_archivo = ""
palabra = ""
palabra_encontrada = False
cantidad_letras = 0

while True:
    try:
        nombre_archivo = input("Ingrese nombre del archivo:")
    except ValueError:
        print("Nombre de archivo inválido")
        continue
    break

while True:
    try:
        palabra = input("Ingrese la palabra a buscar:")
    except ValueError:
        print("Palabra inválida")
        continue
    break

with open(nombre_archivo, "r") as archivo:
    palabras = archivo.read().split()
    for i in range(0, len(palabras)):
        if palabra == palabras[i]:
            palabra_encontrada = True
            break

if palabra_encontrada:
    print("La palabra se encuentra en el archivo")
else:
    print("La palabra no se encuentra en el archivo")
