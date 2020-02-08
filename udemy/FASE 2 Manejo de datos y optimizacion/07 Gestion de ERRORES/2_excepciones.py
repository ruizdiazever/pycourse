# Funcion para marcar ejercicios
def mensaje(num):
    print("\nEJERCICIO",num)


# EJERCICIO 1
mensaje(1)
while(True):
    try:
        num = int(input("Introduzca un numero: "))
        num_2 = 10
        print("{} dividido {} es {}".format(num,num_2,num/num_2))
    except:
        print("Ha ocurrido un error, tiene que introducir un numero.")
    else:
        print("Todo ha funcionado correctamente.")
        break # Importante romper la iteracion si todo ha salido bien.

# EJERCICIO 2
mensaje(2)
while(True):
    try:
        num = int(input("Introduzca un numero: "))
        num_2 = 10
        print("{} dividido {} es {}".format(num,num_2,num/num_2))
    except:
        print("Ha ocurrido un error, tiene que introducir un numero.")
    else:
        print("Todo ha funcionado correctamente.")
        break # Importante romper la iteracion si todo ha salido bien.
    finally:
        print("Fin de la iteracion.")


# Encadenar un bloque else a un except nos permite ejecutar código si no se ejecuta la excepción, actuando en este caso el except como un if.
