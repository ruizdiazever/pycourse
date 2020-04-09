""" Python 3.6: Format simplificado
La nueva gran actualización de Python 3.6 fue liberada a finales de Diciembre de 2016. 
Esta actualización trae muchas novedades avanzadas y no afecta en nada a este curso, 
pero hay una muy interesante que estoy seguro que os gustará. 

Se trata de la posibilidad de concadenar variables y cadenas de una forma muy cómoda 
sin utilizar el format:

Hasta ahora para concadenar hacíamos lo siguiente: """

nombre = "Héctor"
texto = "Hola {}".format(nombre)
print(texto)

""" La nueva sintaxis nos permite ahorrarnos el format: """

nombre = "Héctor"
texto = f"Hola {nombre}"
print(texto)