numbers = [1,2,3,4,5,6,7,8,9,10]

# EJEMPLO 1 CON WHILE
print("EJEMPLO 1: WHILE")
index = 0
while (index < len(numbers)):
    print(numbers[index])
    index+=1

# EJEMPLO 2 CON FOR
print("EJEMPLO 2: FOR")
for number in numbers:
    print(number)

# EJEMPLO 3
print("EJEMPLO 3")
indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)

# EJEMPLO 4 IMPORTANTE! ENUMERATE
print("EJEMPLO 4")
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice, numero in enumerate(numeros): # enumerate tiene que recibir algo para iterar como argumento
    # indice es la posicion, numero es el valor
    numeros[indice] *= 10
print(numeros)

# EJEMPLO 4: ENUMERATE
lista = [5,5,10,500]

for posicion, numero in enumerate(lista):
    lista[posicion] *= 10
    print("En la posicion {} el numero obtenido es {}".format(posicion,lista[posicion]))

# EJEMPLO 5
print("EJEMPLO 5")
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)

# EJEMPLO 6
print("EJEMPLO 6")
cadena_2 = ""
for caracter in cadena:
    cadena_2 += caracter * 2
print(cadena_2)

# EJEMPLO 7
print("EJEMPLO 7")
for i in range(10):
    print(i)
print(range(10)) # De 0 a 10, no ocupa memoria

# EJEMPLO 8
print("EJEMPLO 8")
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
print(list(range(10)))