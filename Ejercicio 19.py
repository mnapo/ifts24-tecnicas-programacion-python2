# remover duplicados de una lista

def elimina_duplicados(lista):
  lista_sin_duplicados = []
  for i in range(0, len(lista)):
    elemento = lista[i]
    if (elemento in lista_sin_duplicados) == False:
      lista_sin_duplicados.append(elemento)
  return lista_sin_duplicados
