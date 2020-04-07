# Es una funcion que envuelve la ejecucion de otra funcion y permite
# extender su comportamiento.

# Funcion decoradora:
def monitorizar(funcion):
    def decorar():
        print("\t Se esta apunto de ejecutar la funcion:", funcion.__name__)
        funcion()
        print("\t Se ha finalizado la ejecucion de la funcion: ", funcion.__name__)
    return decorar

@monitorizar
def hello():
    return "Hello!"

@monitorizar
def bye():
    return "Good Bye!"

@monitorizar
def saludar():
    return "Como estas?"

hello()
bye()
saludar()