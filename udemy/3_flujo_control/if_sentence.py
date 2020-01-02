# EJEMPLO 1
print("EJEMPLO 1")
if True:
    print("Se cumple la condicion.")
    print("Tambien se muestra este print")
if False: # NUNCA ENTRA, NO MUESTRA
    print("Se cumple la condicion.")
    print("Tambien se muestra este print")
if not False: # ENTRA
    print("Se cumple la condicion.")
    print("Tambien se muestra este print")
print("\n")

# EJEMPLO 2
print("EJEMPLO 2")
a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")
print("\n")

# EJEMPLO 3
print("EJEMPLO 3")
b = 7
c = 10
if b == 7:
    print("b vale",b)
    if c == 10:
        print("y c vale",c)
print("\n")

# EJEMPLO 3.1 (ALTERNATIVO)
print("EJEMPLO 3.1, ALTERNATIVA")
if b == 7 and c == 10:
    print("b es igual a",b,"y c es igual a",c)
print("\n")

# EJEMPLO 4
print("EJEMPLO 4")
n = 10
if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n, "es un numero impar")
print("\n")

# EJEMPLO 5 (ELIF= SINO SI)
print("EJEMPLO 5")
comando = "SALIR"
if comando == "ENTRAR":
    print("Bienvenido al sistema.")
elif comando == "SALUDAR":
    print("Hola, este es tu perfil.")
elif comando == "SALIR":
    print("Saliendo del sistema, hasta pronto.")
else:
    print("Este comando no se reconoce.")
print("\n")

# EJEMPLO 6
print("EJEMPLO 6")
nota = float(input("Introduce una nota: "))
if nota >= 9 and nota < 11:
    print("Sobresaliente")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 5 and nota < 6:
    print("Suficiente")
elif nota < 5:
    print("Insuficiente")
else:
    print("Numero incorrecto.")
print("\n")

# EJEMPLO 7
print("EJEMPLO 7")
if True:
    pass
