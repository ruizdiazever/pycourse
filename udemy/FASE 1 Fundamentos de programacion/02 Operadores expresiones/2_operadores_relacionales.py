# Igual que
3 == 2

# Distinto
3 != 2

# Mayor que
3 > 2

# Menor que
3 < 2

# Mayor o igual que
3 >= 4

# Menor o igual que
3 <= 3


# Ejemplo 1
c = "Hola"
print("Ejemplo 1.0=",c[0]=="H")
print("Ejemplo 1.1=",c[-1]=="a", "\n")

# Ejemplo 2
list_1 = [1,2,5]
list_2 = [4,5,6]
print("Ejemplo 2.0=", list_1 == list_2) # Son iguales?
print("Ejemplo 2.1=", len(list_1)==len(list_2)) # Misma longitud?
print("Ejemplo 2.2=", list_1[-1] == list_2[1], "\n") # Elementos iguales?

# Ejemplo 3
a = 10
b= int(input("Ingrese un numero: "))
if a == b*2:
    print("A es IGUAL a Bx2.", "\n")
else:
    print("A es DISTINTO de Bx2.", "\n")

# Ejemplo 4
print("Ejemplo 4= ",True == True)
print("Ejemplo 4.1=", True != False)
print("Ejemplo 4.2=",True > False) # True es mayor que False?
print("Ejemplo 4.3=",False > True) # False es mayor que True?
# IMPORTANTE= True = 1 y False = 0