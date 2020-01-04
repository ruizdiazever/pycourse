# 2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetise el proceso hasta que lo introduzca correctamente.

impar = int(input("Ingrese un numero impar: "))

while impar % 2 == 0:
    print("Numero par, introduzca nuevamente.")
    impar = int(input("Ingrese un numero impar: "))
else:
    print("Numero impar ingresado correctamente.")