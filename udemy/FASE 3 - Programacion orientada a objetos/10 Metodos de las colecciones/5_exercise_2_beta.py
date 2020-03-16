# 2) Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:**
    # * Borrar los elementos duplicados
    # * Ordenar la lista de mayor a menor
    # * Eliminar todos los números impares
    # * Realizar una suma de todos los números que quedan
    # * Añadir como primer elemento de la lista la suma realizada
    # * Devolver la lista modificada
    # * Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo,
    # concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print("Ejemplo: ", lista)

def modificar(lista):
    lista = set(lista) # Borramos los elementos duplicados
    lista = list(lista) # Convertimos el conjunto en lista
    lista.sort(reverse=True) # Ordenamos la lista de menor a mayor
    # Eliminamos todos los numeros impares
    lista_2 = []
    for i in lista:
        if (i % 2) == 0:
            lista_2.append(i)
        else:
            pass
    lista.clear() # Vaciamos la lista
    lista = lista_2.copy() # Copiamos la lista_2 en lista
    suma = sum(lista) # Realizamos una suma de todos los números que quedan
    lista.insert(0,suma) # Añadir como primer elemento de la lista la suma realizada
    print("======================================")
    print("Suma de los numeros: ",suma)
    print("Lista modificada: ", lista) # Devolver la lista modificada
    print("Coincide la primera posicion con la suma del restante?: ", lista[0] == sum(lista[1:]))
    if (lista[0] == sum(lista[1:])):
        print("La suma coincide.")
        print("======================================")
    else:
        print("La suma no coincide.")
        print("======================================")



modificar(lista)