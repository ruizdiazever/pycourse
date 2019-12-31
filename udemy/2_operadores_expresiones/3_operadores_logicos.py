# Ejemplo 1
print("1.1:",not True)
print("1.2:",not True == False, "\n")

# Ejemplo 2
# CONJUNCION: viene del conjunto, sinonimo de unido, contiguo o cercano, agruna uniendo.
# DINYUNCION: viene de disyunto, sinonimo de separado, apartado o distante, agrupa separando.
print("2.1:", True and True)
print("2.2:", True and False) # Lo mismo alreves
print("2.3:", False and False, "\n") # False

# Ejemplo 3
a = int(input("Ingrese un numero: "))
if a > 10 and (a < 20):
    print("3.1: Verdadero")
else:
    print("3.2: Falso")