# https://docs.hektorprofe.net/python/funcionalidades-avanzadas/funciones-generadoras/
def separador(num):
    print("\n************** {} **************".format(num))

# Por regla general, cuando queremos crear una lista de algún tipo, 
# lo que hacemos es crear la lista vacía, y luego con un bucle varios 
# elementos e ir añadiendolos a la lista si cumplen una condición:

separador(1)
lista = [numero for numero in [0,1,2,3,4,5] if numero % 2 == 0] # sin generador
print(lista)

separador(2)
lista= [numero for numero in range(0,11) if numero % 2 == 0] # 'range' es un generador
print(lista)

separador(3)
def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero

for numero in pares(10):
    print(numero)

separador(4)
print(pares(10))
print([numero for numero in pares(10)])

# Función integrada next() nos permite acceder al siguiente elemento de la 
# secuencia. Pero no sólo eso, si volvemos a ejecutarla...
separador(5)
pares = pares(3)
print(next(pares))
print(next(pares))


separador(6)
# No podemos iterar ninguna colección como si fuera una secuencia. Sin embargo, 
# hay una función muy interesante que nos permite covertir las cadenas y algunas 
# colecciones a iteradores, la función iter():
lista = [1,2,3,5,5]
lista_iterable = iter(lista)
print(lista_iterable)
print(next(lista_iterable))

separador(7)
# con cadenas
cadena = "HANNAH"
cadena_i = iter(cadena)
print(next(cadena_i))
print(next(cadena_i))
print(next(cadena_i))
print(next(cadena_i))
print(next(cadena_i))
print(next(cadena_i))