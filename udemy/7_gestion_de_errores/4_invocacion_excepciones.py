# La instrucción raise
# Gracias a raise podemos lanzar un error manual pasándole el identificador. 
# Luego simplemente podemos añadir un except para tratar esta excepción que hemos lanzado:
def mi_funcion(algo=None):
    try:
        if algo == None:
            raise ValueError("Error! No se permite un valor nulo.")
    except ValueError:
        print("Error! No se permite un valor nulo")
mi_funcion()