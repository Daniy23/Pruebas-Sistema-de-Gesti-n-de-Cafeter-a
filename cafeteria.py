import pytest


def validar_entrada(entrada):
  # Eliminar espacios en blanco
  entrada = entrada.replace(" ", "")

  # Intentar dividir la entrada en nombre y tamaños
  try:
    nombre, tamanos_str = entrada.split(",", 1)
  except ValueError:
    return False

  if not nombre.isalpha() or len(nombre) < 2 or len(nombre) > 15:
    return False

  tamanos = tamanos_str.split(",")
  try:
    tamanos = [int(size) for size in tamanos]
  except ValueError:
    return False

  if len(tamanos) < 1 or len(tamanos) > 5:
    return False
  if not all(1 <= size <= 48 for size in tamanos):
    return False
  if tamanos != sorted(tamanos):
    return False

  return True


# Ejemplo de uso
# entrada = input("Entrada: ") # Remove this line
entrada = "Daniela"  # Example input for testing
if validar_entrada(entrada):
  print("Entrada válida.")
else:
  print("Entrada inválida.")


def test_validar_entrada():
  # 1. El nombre del artículo es alfabético (válido)
  assert validar_entrada("Cafe,36,38,40") == True

  # 2. El nombre del artículo tiene menos de 2 caracteres de longitud (inválido)
  assert validar_entrada("C,36,38,40") == False

  # 3. El nombre del artículo tiene de 2 a 15 caracteres de longitud (válido)
  assert validar_entrada("Taro, 42") == True

  # 4. El valor del tamaño está en el rango de 1 a 48 (válido)
  assert validar_entrada("Chocolate,36,38,40") == True

  # 5. El valor del tamaño es un número entero (válido)
  assert validar_entrada("Te,39") == True

  # 6. Los valores del tamaño se ingresan en orden ascendente (válido)
  assert validar_entrada("Agua,32,34,36,38,40") == True

  # 7. Se ingresan de uno a cinco valores de tamaño (válido)
  assert validar_entrada("Expreso,1,2,3,4,5") == True

  # 8. El nombre del artículo es el primero en la entrada (válido)
  assert validar_entrada("Frappuccino, 42") == True

  # 9. Una sola coma separa cada entrada en la lista (válido)
  assert validar_entrada("CaféCortado, 36, 38, 40") == True

  # 10. La entrada contiene o no espacios en blanco (a especificar en las pruebas)
  assert validar_entrada("Caramel Machiato,36,38,40") == True


 
