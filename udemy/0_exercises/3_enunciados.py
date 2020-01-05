# 1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#       Mostrar una suma de los dos números
#       Mostrar una resta de los dos números (el primero menos el segundo)
#       Mostrar una multiplicación de los dos números
#       En caso de no introducir una opción válida, el programa informará de que no es correcta.
num_1 = float(input("1. Introduzca un numero: "))
num_2 = float(input("2. Introduzca un numero: "))

option = int(input("""Introduzca una opcion:
1. Suma.
2. Resta
3. Multiplicacion.
Ingrese: """))

if option == 1:
    print("Suma: ",num_1+num_2)
elif option == 2:
    print("Resta: ",num_1-num_2)
elif option == 3:
    print("Multiplicacion: ",num_1*num_2)
else:
    print("Opcion invalida, ingrese nuevamente.")



# 2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetise el proceso hasta que lo introduzca correctamente.
impar = int(input("Ingrese un numero impar: "))
while impar % 2 == 0:
    print("Numero par, introduzca nuevamente.")
    impar = int(input("Ingrese un numero impar: "))
else:
    print("Numero impar ingresado correctamente.")



# 3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
#       Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. 
#       El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
lista = []

for i in range(0, 101, 1):
    if i % 2 == 0:
        lista.append(i)
print(lista)

suma = sum(lista)
print(suma)



# 4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
num = int(input("Introduzca la cantidad numeros que va a sacar el promedio: "))
lista = []

while len(lista) < num:
    num_2 = int(input("Introduzca un numero: "))
    lista.append(num_2)
print(lista)
suma=sum(lista)
promedio=suma/num
print("El promedio es: ", promedio)


# 5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
#       Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)
#       numeros = [1, 3, 6, 9]
num = int(input("Introduzca un numero del 0 al 9: "))
numeros = [1, 3, 6, 9]

while num > 9 or num < 0:
    print("Numero incorrecto, introduzca nuevamente: ")
    num = int(input("Introduzca un numero del 0 al 9: "))

if (num in numeros) == True:
    print("Positivo")
else:
    print("Negativo")


# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#    Todos los números del 0 al 10 0, 1, 2, ..., 10
#    Todos los números del -10 al 0 -10, -9, -8, ..., 0
#    Todos los números pares del 0 al 20 0, 2, 4, ..., 20
#    Todos los números impares entre -20 y 0 -19, -17, -15, ..., -1
#    Todos los números múltiples de 5 del 0 al 50 0, 5, 10, ..., 50
#    Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).
# 1
for num_1 in range(0,11,1):
    print(num_1)
# 2
for num_2 in range(-10,1,1):
    print(num_2)
# 3
for num_3 in range(0,21,2):
    print(num_3)
# 4
for num_4 in range(-19,1,2):
    print(num_4)
# 5
for num_5 in range(0,51,5):
    print(num_5)


# 7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
list_1 = [0,1,2,3,4,5]
list_2 = [5,0,2,10,45]
list_3 = []

for num in list_1:
    if (num in list_1) == (num in list_2):
        list_3.append(num)
print(list_3)