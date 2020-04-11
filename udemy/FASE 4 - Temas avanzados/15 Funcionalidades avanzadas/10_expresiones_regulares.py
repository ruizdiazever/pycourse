""" https://docs.hektorprofe.net/python/funcionalidades-avanzadas/expresiones-regulares/

Una de las tareas más utilizadas en la programación es la búsqueda de subcadenas o 
patrones dentro de otras cadenas de texto.

Las expresiones regulares, también conocidas como 
    'regex' o 'regexp'
son patrones de búsqueda definidos con una sintaxis formal. Siempre que sigamos sus 
reglas, podremos realizar búsquedas simples y avanzadas, que utilizadas en conjunto 
con otras funcionalidades, las vuelven una de las opciones más útiles e importantes 
de cualquier lenguaje. """

import re

texto = "En esta cadena se encuentra una palabra magica"


print("=================== EJEMPLO 1 're.search()' ===================")
print("1.   ", re.search('magica', texto)) # re.search busca un patron en una cadena
print("2.   ", re.search('godzilla', texto)) # None



print("\n=================== EJEMPLO 2 're.searh()' ===================")
palabra = "magica"
encontrado = re.search(palabra, texto)

if palabra is not None:
    print("Palabra encontrada")
else:
    print("Palabra no encontrada")


print("\n=================== EJEMPLO 3 're.start()' ===================")
# Posición donde empieza la coincidencia
print(encontrado.start()) # Linea 25,26
print("=================== EJEMPLO 4 're.end()' ===================")
# Posición donde termina la coincidencia
print(encontrado.end())
print("=================== EJEMPLO 5 're.span()' ===================")
# Tupla con posiciones donde empieza y termina la coincidencia
print(encontrado.span())
print("=================== EJEMPLO 6 're.string()' ===================")
# Cadena sobre la que se ha realizado la búsqueda
print(encontrado.string)





print("\n=================== EJEMPLO 7 're.match()' ===================")
# re.match: busca un patrón al principio de otra cadena:
texto = "Hola marte"
ma = re.match("Hola", texto)
me = re.match("Adios", texto) # Cadena que no existe
print("1.   ", ma)
print("2.   ", me)




print("\n=================== EJEMPLO 8 're.split()' ===================")
# re.split: dividir una cadena a partir de un patron
texto = "Vamos a dividir esta cadena"
texto = re.split(" ", texto)
print(texto)


print("\n=================== EJEMPLO 9 're.sub()' ===================")
texto = "Hola amigo"
texto = re.sub("amigo","amiga", texto)
print(texto)


print("\n=================== EJEMPLO 10 're.findall()' ===================")
texto = "hola adios hola hola"
repes = re.findall('hola', texto)
print(repes) # tres veces en una lista..
repes = re.findall('a', texto)
print(len(repes)) # IMPORTANTEEEEEEEEEEEEEEE


print("\n=================== EJEMPLO 11 're.findall()' ===================")
texto = "hola hello bye hola"
repes = re.findall("hola|hello", texto)
print(repes)


""" Documentación
Hay docenas y docenas de códigos especiales, si queréis echar un vistazo a todos ellos podéis consultar la documentación oficial:

https://docs.python.org/3.5/library/re.html#regular-expression-syntax
Un resumen por parte de Google Eduactión:

https://developers.google.com/edu/python/regular-expressions
Otro resumen muy interesante sobre el tema:

https://www.tutorialspoint.com/python/python_reg_expressions.htm
Un par de documentos muy trabajados con ejemplos básicos y avanzados:

http://www.python-course.eu/python3_re.php
http://www.python-course.eu/python3_re_advanced.php """