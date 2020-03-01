# Ejemplo 1
print("1.1:",not True)
print("1.2:",not True == False, "\n")

# Ejemplo 2
# CONJUNCION(AND): viene del conjunto, sinonimo de unido, contiguo o cercano, agrupa uniendo.
# DINYUNCION(OR): viene de disyunto, sinonimo de separado, apartado o distante, agrupa separando.
print("2.1:", True and True)
print("2.2:", True and False) # Lo mismo alreves
print("2.3:", False and False, "\n") # False

# Ejemplo 3
# a = int(input("Ingrese un numero: "))
a = 11
if a > 10 and (a < 20):
    print("3.1: True", "\n")
else:
    print("3.2: False", "\n")

# Ejemplo 4
string = "Hola mundo"
if (len(string) >= 15) and (string[0] == "H"):
    print("4.1: True", "\n")
else:
    print("4.2: False", "\n")

# Ejemplo 5
string = "Hola mundo"
if (len(string) >= 15) or (string[0] == "H"):
    print("5.1: True", "\n")
else:
    print("5.2: False", "\n")

# Ejemplo 6
print("6.1:", True or False)
print("6.2:", False or True)
print("6.3:", False or False, "\n")

# Ejemplo 7
c = "Salir"
print("7.1:", c == "Salir" or c == "Exit" or c == "Fin")