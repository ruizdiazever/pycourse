# Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. En estos casos podemos utilizar los parámetros indeterminados por posición y por nombre.

# POR POSICION: para recibir un número indeterminado de parámetros por posición, debemos crear una lista dinámica de argumentos (una tupla en realidad).
# PARAMETROS ITERABLES
print("\nParametros iterables")
def indeterminados_posicion(*args): # Parametro iterable
    print(args)
    for arg in args:
        print(arg)
indeterminados_posicion(5, "Hola", [1, 5, 3, 10]) # Devuelve tupla


# POR NOMBRE: para recibir un número indeterminado de parámetros por nombre (clave-valor), debemos crear un diccionario dinámico de argumentos.
# PARAMETROS POR CLAVE: DICCIONARIO
print("\nParametros con nombre")
def indeterminados_nombre(**kwargs): # KEY WORDS ARGS
    print(kwargs)
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])

indeterminados_nombre(n=5,c="Hola",l=[1, 5, 3, 10])


# POR POSICION Y NOMBRE A LA VEZ: si queremos aceptar ambos tipos de parámetros simultáneamente, entonces debemos crear ambas colecciones dinámicas:
# PARAMETROS MIXTOS
def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es", t)
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])
        
super_funcion(10, 50, -1, 1, -56, nombre="Hector", edad=27)
