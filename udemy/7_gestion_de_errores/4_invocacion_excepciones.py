def mi_funcion(algo=None):
    try:
        if algo == None:
            raise ValueError("Error! No se permite un valor nulo.")
    except ValueError:
        print("Error! No se permite un valor nulo")
mi_funcion()