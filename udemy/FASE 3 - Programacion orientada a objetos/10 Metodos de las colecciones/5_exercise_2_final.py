lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Completa el ejercicio aquí

def modificar(l):
    # Borrar los elementos duplicados (haciendo conversión a conjunto)
    l = list(set(l))
    # Ordenar la lista de mayor a menor
    l.sort(reverse=True)

    # Lista temporal que contendrá solo los números pares
    l_tmp = []
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)

    # Realizar una suma de todos los números que quedan
    suma = sum(l_tmp)
    # Añadir como primer elemento de la lista de pares la suma realizada
    l_tmp.insert(0, suma)
    # Devolver la lista de pares modificada
    return l_tmp


nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )