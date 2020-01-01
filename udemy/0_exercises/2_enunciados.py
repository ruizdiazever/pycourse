# 1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos 
# (es suficiene con mostrar True o False):
#       Si los dos números son iguales
#       Si los dos números son diferentes
#       Si el primero es mayor que el segundo
#       Si el segundo es mayor o igual que el primero

# 2) Utilizando operadores lógicos, determina si una cadena de texto introducida por el 
# usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False):

# 3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
#       Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#       Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
#       Multiplica el numero_usuario por 9 en sí mismo
#       Multiplica el numero_magico por el numero_usuario en sí mismo
#       Finalmente muestra el valor final del numero_magico por pantalla

num = float(input("1. Ingrese un numero: "))
num_2 = float(input("2. Ingrese un numero: "))
print("\n")

# EJERCICIO 1
print("EJERCICIO 1")
print("1.1 son iguales? ",num == num_2)
print("1.2 son diferentes? ",num != num_2)
print("1.3 primer numero es mayor? ",num > num_2)
print("1.4 segundo numero es mayor o igual? ",num_2 >= num)

# Ejercicio 2
print("EJERCICIO 2")
string = input("Ingrese un texto: ")
print("2. Longitud igual o mayor que 3 y menor que 10?", len(string) >= 3 and len(string) < 10)
print("\n")

# Ejercicio 3
print("EJERCICIO 3")
numero_magico = 12345679
numero_usuario = int(input("Introduzca un numero del 1 a 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print("3. Numero magico es: ", numero_magico)