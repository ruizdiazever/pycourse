# OPERADORES ENCADENADOS
# Una de las pecualiaridades más interesantes de Python, y 
# que otros lenguajes no ofrecen, es la capacidad de encadenar múltiples expresiones.


# LOGICA CORRECTA
3 > 2 > 1
(3 > 2) and (2 > 1)
True and True
True

# LOGICA INCORRECTA
3 > 2 > 1
(3 > 2) > 1
True > 1
False


# Veamos en ejemplo mucho más útil, donde queremos comprobar si un número se encuentra 
# entre 0 y 100 (ambos incluidos):
numero = 35
if numero >= 0 and numero <= 100:
    print("El número {} se encuentra entre 0 y 100".format(numero) )
else:
    print("El número {} no se encuentra entre 0 y 100".format(numero) )


# Utilizando operadores encadenados podemos simplificar la sintaxis readaptando la lógica:
numero = 35
if 0 <= numero <= 100:
    print("El número {} se encuentra entre 0 y 100".format(numero) )
else:
    print("El número {} no se encuentra entre 0 y 100".format(numero) )