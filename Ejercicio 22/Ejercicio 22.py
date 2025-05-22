palabras = []

with open("texto.txt", "r") as archivo:
    palabras = archivo.read().split()

print(palabras)
