# definir función para calcular longitud de lista o cadena

def longitud(objetivo):
  if isinstance(objetivo, str) or isinstance(objetivo, list):
    return len(objetivo)
  return 0
