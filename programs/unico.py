no_repetidos = [1,2,3,4,1000,"Ever"]

def funcion_norepetir(lista, elemento):
    try:
        if elemento in lista:
            print("Error, elemento existente.")
            print("Introduzca un elemento inexistente.")
        else:
            lista.append(elemento)
    except ValueError:
        print("Elemento invalido, vuelva a intentar.")

funcion_norepetir(no_repetidos,"Ever")
print(no_repetidos)