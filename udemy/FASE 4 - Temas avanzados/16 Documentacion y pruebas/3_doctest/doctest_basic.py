"""
Si por un lado las docstrings nos permitían describir documentación, los doctest 
nos permiten combinar pruebas en la propia documentación.

Este concepto de integrar las pruebas en la documentación nos ayuda a mantener 
las pruebas actualizadas, y además nos sirve como ejemplo de utilización del código, 
ayudándonos a explicar su propósito.

Para utilizar doctests hay que inidicar una línea dentro de la documentación de la 
siguiente forma: >>> 
"""
""" 
De esta Python entenderá que debe ejecutar el contenido dentro del comentario 
como si fuera código normal, y lo hará hasta que encuentre una línea en blanco 
(o llegue al final de la documentación).
"""


def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos

    >>> suma(5,10)
    15
    >>> suma(0,0)
    1
    >>> suma(-5,7)
    2
    """
    return a+b

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())