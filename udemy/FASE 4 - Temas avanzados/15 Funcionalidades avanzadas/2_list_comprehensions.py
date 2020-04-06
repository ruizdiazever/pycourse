# Comprensión de listas
    # El poder de Python va mucho más allá de lo que a primera vista 
    # podemos imaginar.

# La comprensión de listas, del inglés list comprehensions, es 
    # una funcionalidad que nos permite crear listas avanzadas en una 
    # misma línea de código. Esto se ve mucho mejor en la práctica, 
    # así que a lo largo de esta lección vamos a trabajar distintos 
    # ejemplos.

# Crear una lista con las letras de una palabra:
# Método tradicional
print("=================== EJEMPLO 1 ===================")
lista = []
for letra in 'casa':
    lista.append(letra)
print(lista)
# Metodo con comprension de listas
lista = [letra for letra in 'casa']
print(lista)



# Crear una lista con las potencias de 2 de los primeros 10 números:
# Metodo tradicional
print("\n=================== EJEMPLO 2 ===================")
lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)
# Metodo con comprension de listas
lista = [numero**2 for numero in range(0,11)]



# Crear una lista con los todos los múltiples de 2 entre 0 y 10:
# Metodo tradicional
print("\n=================== EJEMPLO 3 ===================")
lista = []
for i in range (0,11,2):
    lista.append(i)
print(lista)
# Metodo tradicional II
lista = []
for i in range (0,11):
    if (i % 2) == 0:
        lista.append(i)
print(lista)
# Metodo con comprension de listas
lista = [numero for numero in range(0,11) if numero % 2 == 0 ]
print(lista)



# Crear una lista de pares a partir de otra lista creada con las 
# potencias de 2 de los primeros 10 números:
print("\n=================== EJEMPLO 4 ===================")
# Metodo tradicional
lista = []
for i in range(0,11):
    lista.append(i**2)

pares = []
for numero in lista:
    if (numero % 2) == 0:
        pares.append(numero)
print(pares)
# Metodo con compresion de listas
pares = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 == 0]
print(pares)