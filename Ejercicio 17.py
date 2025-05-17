# decidir si el año es bisiesto

def es_bisiesto(año):
  if (año%4==0 and año%100!=0):
    return True
  return False
