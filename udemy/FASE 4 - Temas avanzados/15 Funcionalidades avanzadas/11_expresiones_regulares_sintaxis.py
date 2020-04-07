# Patrones con sintaxis repetida
# Otra posibilidad que se nos ofrece es la de buscar patrones con 
# letras repetidas, y aquí es donde se empieza a poner interesante. 
# Como podemos o no saber de antemano el número de repeticiones hay 
# varias formas de definirlos.
import re


texto = "cuak hla hola hoola hoooooola"



print("=========== EJEMPLO ===========")
repes = re.findall("hla", texto)
print("1.   ", len(repes))

print("\n=========== SUPERFUNCION ===========")
def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

patrones = ["hla", "hola", "hoola", "hoooooola"]
buscar(patrones, texto)


print("\n=========== METACARACTER * ===========")
# NINGUNA o MAS repeticiones de la letra a su izquierda
# "cuak hla hola hoola hoooooola"

# SIN METACARACTER
patrones = ["ho"]
buscar(patrones, texto)

# CON METACARACTER
patrones = ['ho', 'ho*', 'ho*la', 'hu*la']
buscar(patrones, texto)



print("\n=========== METACARACTER + ===========")
# UNA o MAS repeticiones de la letra a la izquierda del meta-carácter
# "cuak hla hola hoola hoooooola"
patrones = ['ho*', 'ho+']  
buscar(patrones, texto)


print("\n=========== METACARACTER ? ===========")
# UNA o NINGUNA repetición de la letra a la izquierda del meta-carácter
# "cuak hla hola hoola hoooooola"
patrones = ['ho*', 'ho+', 'ho?', 'ho?la']  

buscar(patrones, texto)


print("\n=========== METACARACTER REPES ===========")
# Con número de repeticiones explícito {n}
# Lo utilizaremos para definir 'n' repeticiones exactas de la letra a la izquierda del meta-carácter:
patrones = ['ho{0}la', 'ho{1}la', 'ho{2}la']

buscar(patrones, texto)


print("\n=========== METACARACTER RANGO {n, m} ===========")
# Lo utilizaremos para definir un número de repeticiones variable entre 'n' y 'm' de la letra a la izquierda del meta-carácter:
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']
# la 'o' de 0 a 1 veces
# la 'o' de 1 a 2 veces
# la 'o' de 2 a 9 veces
buscar(patrones, texto)



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
