def ejercicio(num):
    print("\nEJERCICIO",num)

# 1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
#    programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# PROBLEMA:
#    resultado = 10/0
ejercicio(1)
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Error! Un numero no puede ser dividido por 0")
except Exception as e:
    print(type(e).__name__)

# 2) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que 
#    el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# PROBLEMA:
#   lista = [1, 2, 3, 4, 5]
#   print(lista[10])
ejercicio(2)
try:
    lista = [1, 2, 3, 4, 5]
    print(lista[10])
except IndexError:
    print("Posicion fuera del rango de la lista. Introduzca una posicion valida.")
except Exception as e:
    print(type(e).__name__)

# 3) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que 
#    el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# PROBLEMA:
#   colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
#   colores['blanco']
ejercicio(3)
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    print(colores['blanco'])
except KeyError:
    print("Esta tratando de introducir una clave de diccionario inexistente.")
except Exception as e:
    print(type(e).__name__)

# 4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que 
#    el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# PROBLEMA:
#   resultado = 15 + "20"
ejercicio(4)
try:
    print(resultado = 15 + "20")
except TypeError:
    print("No puede sumarse un INT + STRING")
except Exception as e:
    print(type(e).__name__)

# 5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir 
# ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar 
# un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
#   Error: Imposible añadir elementos duplicados => [elemento].
#   Prueba de agregar los elementos 10, -2, "Hola" a la lista de elementos con la función una vez la has creado y luego muestra su contenido.
#   Nota: Puedes utilizar la sintaxis: elemento in lista
ejercicio(5)
elementos = [1, 5, -2]

def agregar_una_vez(lista,elemento):
    try:
        if elemento in lista:
            raise ValueError
        else:
            lista.append(elemento)
            print(lista)
    except ValueError:
        print("Imposible añadir elementos duplicados =>",elemento)

agregar_una_vez(elementos,5)
agregar_una_vez(elementos,10)
