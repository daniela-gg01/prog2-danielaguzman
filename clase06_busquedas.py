busqueda_lineal(lista, clave):
for i range(len(lista)):
   if lista[i] == clave:
      return i  # Devuelve la posición donde lo encontró
   return -1  # Si no lo encuentra



def busqueda_binaria(lista, clave):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == clave:
            return medio
        elif lista[medio] < clave:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # Si no lo encuentra
