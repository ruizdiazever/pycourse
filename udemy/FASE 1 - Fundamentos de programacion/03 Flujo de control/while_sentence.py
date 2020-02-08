# EJEMPLO 1
print("EJEMPLO 1")
c = 0
while c <= 5:
    c += 1
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale", c, "\n")

# EJEMPLO 2
print("EJEMPLO 2")
d = 0
while d <= 5:
    d += 1
    if d == 2:
        print("Rompemos el bucle cuando d vale", d)
        break
    print("d vale", d)
else:
    print("Se ha completado toda la iteracion y d vale", d, "\n")

# EJEMPLO 3
print("EJEMPLO 3")
e = 0
while e <= 5:
    e += 1
    if e == 2:
        continue # Esto rompe esta iteracion y salta a la otra
    print("e vale", e)
else:
    print("Se ha completado toda la iteracion y e vale", e, "\n")

# EJEMPLO 4
print("EJEMPLO 4")
print("Bienvenido al menu interactivo")
while(True):
    print("""¿Que quiere hacer? Escribe una opcion
    1) Saludar
    2) Sumar dos numeros
    3) Salir
    """)
    option = input()
    if option == '1':
        print("Hola, espero que estes bien.")
    elif option == '2':
        n1 = float(input("1. Ingrese un numero: "))
        n2 = float(input("2. Ingrese un numero: "))
        print("El resultado de la suma es ", n1+n2)
    elif option == '3':
        print("Hasta pronto.")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo.")