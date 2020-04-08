""" En la lección anterior aprendimos que utilizando la función help podemos 
mostrar información formateada por la consola. Pues en realidad esta función 
hace uso del módulo pydoc para generar la documentación a partir de sus docstrings.

Desde la terminal no podemos utilizar la función help, pero sí existe la 
posibilidad de utilizar pydoc de forma similar.

Por ejemplo podemos consultar la documentación de scripts, módulos y
clases utilizando la sintaxis: """

# Ejemplo en CMD:

    # python -m pydoc raw_input



""" Documentación HTML
Una función interesante de Pydoc es que podemos generar la documentación de nuestro 
código utilizando la siguiente sintaxis: """
# Ejemplo en CMD:

    # python -m pydoc -w mi_modulo



""" Ahora con paqueres """
    # python -m pydoc -m mi_paquete .\