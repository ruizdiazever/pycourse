# Conjuntos de caracteres
# Cuando nos interese crear un patrón con distintos carácteres, podemos definir conjuntos entre paréntesis:
# https://docs.hektorprofe.net/python/funcionalidades-avanzadas/expresiones-regulares/

import re

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))


print("=================== EJEMPLO 1 ===================")
texto = "hala hela hila hola hula"

patrones = [
    'h[ou]la',      # busca todas las que tengan una 'o' o una 'u'
    'h[aio]la',     # busca todas las que tengan una 'a','i' o una 'o'
    'h[aeiou]la'    # busca todas las que tengan una 'a' 'e' 'i' 'o' o 'u'
    ]
buscar(patrones, texto)


print("=================== EJEMPLO 2 ===================")
texto = "haala heeela hiiiila hoooooola huuula"

patrones = [
    'h[ae]la',      
    'h[ae]*la',     # Cero o mas repeticiones de 'a|e'
    'h[io]{3,9}'    # 'i' o 'o' que se repitan de 3 a 9 veces
    ]
buscar(patrones, texto)


print("=================== EJEMPLO 3 EXCLUSION [^] ===================")
# Cuando utilizamos grupos podemos utilizar el operador de exclusión ^ para indicar una búsqueda contraria:
texto = "hala hela hila hola hula"

patrones = [
    'h[o]la', 
    'h[^o]la'
    ]
buscar(patrones, texto)



print("\n=================== EJEMPLO 4 RANGOS [-] ===================")
""" Otra característica que hace ultra potentes los grupos, es la capacidad de definir rangos. Ejemplos de rangos:

[A-Z]: Cualquier carácter alfabético en mayúscula (no especial ni número).
[a-z]: Cualquier carácter alfabético en minúscula (no especial ni número).
[A-Za-z]: Cualquier carácter alfabético en minúscula o mayúscula (no especial ni número).
[A-z]: Cualquier carácter alfabético en minúscula o mayúscula (no especial ni número).
[0-9]: Cualquier carácter numérico (no especial ni alfabético).
[a-zA-Z0-9]: Cualquier carácter alfanumérico (no especial). """

texto = "hola h0la Hola mola m0la M0la sdjh sdZd U377 Ysdj"

patrones = [
    'h[a-z]la',
    'h[0,9]la',
    '[A-z]{4}', # que se repita 4 veces
    '[A-Z][A-z0-9]{3}'
]

buscar(patrones, texto)




print("\n=================== EJEMPLO 4 CODIGOS ESCAPADOS \ ===================")
""" 
Si cada vez que quisiéramos definir un patrón variable tuviéramos que 
crear rangos, al final tendríamos expresiones regulares gigantes. Por suerte 
su sintaxis también acepta una serie de caracteres escapados que tienen un 
significo único. Algunos de los más importantes son: 
"""
""" 
\d	numérico
\D	no numérico
\s	espacio en blanco
\S	no espacio en blanco
\w	alfanumérico
\W	no alfanumérico
"""

texto = "Este curso de Python 3 se    publico en el    año 2016"
patrones = [
    r'\d',
    r'\d+',
    r'\D',
    r'\D+',
    r'\s', 
    r'\S+', 
    r'\w+', 
    r'\W+'
    ] 
buscar(patrones, texto)



""" Documentación
Hay docenas y docenas de códigos especiales, si queréis echar un vistazo a todos ellos podéis 
consultar la documentación oficial:

https://docs.python.org/3.5/library/re.html#regular-expression-syntax
Un resumen por parte de Google Eduactión:

https://developers.google.com/edu/python/regular-expressions
Otro resumen muy interesante sobre el tema:

https://www.tutorialspoint.com/python/python_reg_expressions.htm
Un par de documentos muy trabajados con ejemplos básicos y avanzados:

http://www.python-course.eu/python3_re.php
http://www.python-course.eu/python3_re_advanced.php """