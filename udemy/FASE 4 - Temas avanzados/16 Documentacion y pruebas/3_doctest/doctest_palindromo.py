def palindromo(palabra):
    """
    Comprueba si una palabra es un palíndrimo. Los palíndromos son 
    palabras o frases que se leen igual de ambos lados.
    Si es un palíndromo devuelve True y si no False

    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("holah")
    False

    >>> polindromo("Ana")
    True
    >>> polindromo("Atar a la rata")
    True
    """
    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", ""): 
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())


""" En el mundo de la programación hay una práctica conocida como TDD, 
Test Driven Development o Desarrollo guiado por pruebas 
que trata de escribir las pruebas primero y luego refactorizar para 
ir puliendo la funcionalidad. """