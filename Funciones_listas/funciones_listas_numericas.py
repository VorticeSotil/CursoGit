'''
Este script contendrá una función para crear una lista de números que el
usuario introducirá por consola.
El usuario decidirá qué y cuantos numeros introducir, y ademas decidirá
cuando dejar de hacerlo.
'''
def crear_lista_num() -> list:

    print("PROGRAMA PARA CREAR UNA LISTA DE NUMEROS")

    res = input("¿Desea crear una nueva lista? ('s': Sí - Cualquier tecla: No): ")

    if res == "s":

        lista_n = []

        while True:

            while True:

                num = input("\nIntroduzca un nuevo número: ")

                if num.isdigit() == False:
                    print("Se debe introducir un número. Intentalo de nuevo.")
                else:
                    break

            lista_n.append(num)
            
            res = input("¿Desea seguir añadiendo valores? ('s': Sí - Cualquier tecla: No): ")

            if res != "s":
                break

        print(f"\n{lista_n}")

        return lista_n

mi_lista = crear_lista_num()


