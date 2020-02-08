# input es un ejemplo de entrada

# EJEMPLO 1
decimal = float(input("Ingrese un numero decimal con punto: "))
print("El dato ingresado es de tipo:",type(decimal))

# EJEMPLO 2
valores = []
print("Introduce 3 valores:")
for x in range(3):
    valores.append(input("Introduce un valor: "))
print("Los valores de la lista son:",valores)