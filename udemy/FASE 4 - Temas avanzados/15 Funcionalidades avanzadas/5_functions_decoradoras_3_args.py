# Funcion decoradora:
def monitorizar_args(funcion):
    def decorar(*args, **kwargs):
        print("\t Se esta apunto de ejecutar la funcion:", funcion.__name__)
        funcion(*args, **kwargs)
        print("\t Se ha finalizado la ejecucion de la funcion: ", funcion.__name__)
    return decorar


@monitorizar_args
def hello(name):
    print("Hello {}!".format(name))

@monitorizar_args
def bye(name):
    print("Bye {}!".format(name))


hello("Ever")
bye("Argentina")