def suma(a, b):
    """Esta función recibe dos parámetros y devuelve la suma de ambos
    Pueden ser números:
    >>> suma(5,10)
    15

    >>> suma(-5,7)
    2

    Cadenas de texto:
    >>> suma('aa','bb')
    'aabb'

    O listas:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    Sin embargo no podemos sumar elementos de tipos diferentes:
    >>> suma(10,"hola")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a+b

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())