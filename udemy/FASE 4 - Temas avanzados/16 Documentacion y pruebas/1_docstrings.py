def separador(num):
    print("\n==================== PARTE {} ====================".format(num))

# https://docs.hektorprofe.net/python/documentacion-y-pruebas/docstrings/

""" Recordad, una buena documentación siempre dará respuesta a las dos preguntas:

¿Para qué sirve?
¿Cómo se utiliza? """

""" En Python todos los objetos cuentan con una variable especial
llamada doc gracias a la que podemos describir para qué sirven los
y cómo se usan los objetos. Estas variables reciben el nombre de 
docstrings, cadenas de documentación. """
separador(1)
def hola(arg):
    """Este es el docstring de la función"""
    print("Hola", arg, "!")
hola("Ever")



separador(2)
""" Para consultar la documentación es tan sencillo como utilizar 
la función reservada help y pasarle el objeto: """
help(hola)




separador(3)
# Clases y metodos
""" De la misma forma podemos establecer la documentación de la clase después 
de la definición, y de los métodos, como si fueran funciones: """
class Clase:
    """ Este es el docstring de la clase"""
    def __init__(self):
        """Este es el docstring del inicializador de clase"""
        pass
    def metodo(self):
        """Este es el docstring del metodo de clase"""
        pass

o = Clase()
#help(o)



separador(4)
# Scripts y módulos
import mi_modulo
import pprint
mi_modulo.despedir()
mi_modulo.saludar()
help(mi_modulo)
help(mi_modulo.saludar)
# Como dato curioso, también podemos listar las variables y funciones del módulo con dir(): 
pprint.pprint(dir(mi_modulo))
print("1.   ", mi_modulo.__name__)     # Nombre del módulo
print("2.   ", mi_modulo.__doc__)      # Docstring del módulo
print("3.   ", mi_modulo.__package__)  # Nombre del paquete del módulo



separador(5)
# Paquetes: el docstring se declara en el '__init__.py' 
import mi_paquete
help(mi_paquete)



separador(6)
# Ejemplos varios
help(print)
help(len)
import datetime
help(datetime)