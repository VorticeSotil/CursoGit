# PROGRAMA PARA CREAR UN DICCIONARIO DE PAISES Y CAPITALES

def dic_paises_capitales() -> dict:

    print("PROGRAMA PARA CREAR UN DICCIONARIO DE PAISES Y CAPITALES")

    res = input("¿Desea crear un nuevo diccionario? ('s': Sí - Cualquier tecla: No): ")

    if res == "s":

        dic = {}

        while True:

            while True:

                pais = input("Introduzca el país: ")

                if pais.isdigit():
                    print("El país debe ser una cadena de texto")
                else:
                    break

            while True:
                capital = input("Introduzca la capital del país: ")

                if capital.isdigit():
                    print("La capital del país debe ser una cadena de texto")
                else:
                    break


            dic.update({pais: capital})
            
            res = input("¿Desea seguir añadiendo valores? (S: Sí - Cualquier tecla: No): ")

            if res != "s":
                break

        print(dic)

        return dic


mi_dic = dic_paises_capitales()















