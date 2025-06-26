'''
Haga un programa que permita generar un menú de gestión de entradas para el
Teatro CafeConLeche con la función “Cats” y sus distintos musicales. El menú
principal debe permitir mostrar 4 opciones:

TOTEM AUTOATENCIÓN CAFECONLECHE
1.- Comprar entrada a Cats.
2.- Cambio de función.
3.- Mostrar stock de funciones.
4.- Salir

Todas las opciones del menú deben estar implementadas mediante funciones se-
paradas del código principal (main).
Al ingresar a la opción 1.- Comprar entrada, se debe permitir ingresar nombre de
comprador y selección de función por separado. Para que la compra sea exitosa
se debe cumplir lo siguiente:
a) El nombre de comprador no debe estar repetido,
b) La selección de la función debe permitir seleccionar entradas para una de las dos
funciones.

Función 1: Cats Día Viernes.
Función 2: Cats Día Sábado.

c)  Debe haber un máximo de 150 entradas para la función 1, y 180 entradas para la
función 2.
'''






funcion_1 = 150

funcion_2 = 180

compradores = {}


def mostrar_menu():

  print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")

  print("1.- Comprar entrada a Cats.")

  print("2.- Cambio de función.")

  print("3.- Mostrar stock de funciones.")

  print("4.- Salir.")


def pedir_opcion_valida():

  while True:

    opcion = input("Seleccione una opción: ")

    if opcion in ['1', '2', '3', '4']:

      return int(opcion)

    else:

      print("Debe ingresar una opción válida!!")



# Función para comprar entrada

def comprar_entrada():

  global funcion_1, funcion_2, compradores



  print("-- Comprar entrada a Cats --")

  while True:

    nombre = input("Nombre del comprador: ").strip()

    if nombre == "":

      print("Nombre no puede estar vacío.")

    elif nombre in compradores:

      print("Error: el nombre ya está registrado.")

    else:

      break



  print("Seleccione función:")

  print(f"1. Cats Día Viernes ({funcion_1} entradas)")

  print(f"2. Cats Día Sábado ({funcion_2} entradas)")



  while True:

    funcion = input("Función (1 ó 2): ")

    if funcion == "1":

      if funcion_1 > 0:

        compradores[nombre] = 1

        funcion_1 -= 1

        print("Entrada registrada en función 1! Stock restantes:")

        mostrar_stock()

      else:

        print("No hay stock disponible para función 1.")

      break

    elif funcion == "2":

      if funcion_2 > 0:

        compradores[nombre] = 2

        funcion_2 -= 1

        print("Entrada registrada en función 2! Stock restantes:")

        mostrar_stock()

      else:

        print("No hay stock disponible para función 2.")

      break

    else:

      print("Error: opción de función inválida.")



# Función para cambio de función

def cambio_funcion():

  global funcion_1, funcion_2, compradores



  print("-- Cambio de función --")

  nombre = input("Nombre del comprador: ").strip()

  if nombre not in compradores:

    print("Error: comprador no encontrado.")

    return



  funcion_actual = compradores[nombre]

  nueva_funcion = 2 if funcion_actual == 1 else 1



  print(f"Cambiar de función {funcion_actual} a {nueva_funcion}? (S/N): ", end="")

  respuesta = input().strip().lower()

  if respuesta != "s" and respuesta != "si":

    print("Cambio cancelado.")

    return



  if nueva_funcion == 1 and funcion_1 > 0:

    compradores[nombre] = 1

    funcion_1 -= 1

    funcion_2 += 1

    print("Cambio realizado a función 1.")

  elif nueva_funcion == 2 and funcion_2 > 0:

    compradores[nombre] = 2

    funcion_2 -= 1

    funcion_1 += 1

    print("Cambio realizado a función 2.")

  else:

    print("No hay stock disponible para el cambio.")



# Función para mostrar el stock actual

def mostrar_stock():

  vendidos_1 = 150 - funcion_1

  vendidos_2 = 180 - funcion_2

  print("-- Stock de Funciones --")

  print(f"Función 1 (Viernes): Disponibles {funcion_1}, Vendidas {vendidos_1}")

  print(f"Función 2 (Sábado): Disponibles {funcion_2}, Vendidas {vendidos_2}")



# Función principal (main)

def main():

  while True:

    mostrar_menu()

    opcion = pedir_opcion_valida()



    if opcion == 1:

      comprar_entrada()

    elif opcion == 2:

      cambio_funcion()

    elif opcion == 3:

      mostrar_stock()

    elif opcion == 4:

      print("Programa terminado...")

      break


main()