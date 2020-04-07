# https://docs.hektorprofe.net/python/funcionalidades-avanzadas/funciones-decoradoras/

# No cabe duda de que Python es un lenguaje flexible, y cuando trabajamos con funciones 
# no es una excepción.

# En Python, dentro de una función podemos definir otras funciones. 
# Con la peculiaridad de que el ámbito de estas funciones se encuentre únicamente 
# dentro de la función padre. Vamos a trabajar los ámbitos un poco más en profundidad:

lista = [1,2,3]

def hola(): # Ambito GLOBAL
    numero = 50

    def bienvenido(): # Ambito LOCAL
        return "Hola!"

    print(locals())
    print(globals())

    return bienvenido

print(hola())
globals().keys() # Devolvemos solo las llaves
print(globals()['lista']) # Invocamos por clave
print(hola()()) # Por muy raro que parezca, podríamos ejecutarla llamando una segunda vez al paréntesis. La primera para hola() y la segunda para bienvenido():


# Si ya era extraño ejecutar funciones anidadas, todavía es más extraño el concepto de 
# enviar una función como argumento de otra función, sin embargo gracias a la flexibilidad 
# de Python es posible hacerlo:

def hello():
    return "Hi!"
def test(funcion):
    print(funcion())
test(hola)