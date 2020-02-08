texto_1 = "Hola mundo"
texto_2 = 'Hola mundo'
texto_3 = 'Este texto incluye unas "" '
texto_4 = "Este texto incluye unas '' "
texto_5 = "Esta \"palabra\" se encuentra escrita entre comillas"
texto_6 = "Esta \'palabra\' se encuentra escrita entre comillas"

print("PARTE 1: ")
print("Texto 1: ", texto_1)
print("Texto 2: ", texto_2)
print("Texto 3: ", texto_3)
print("Texto 4: ", texto_4)
print("Texto 5: ", texto_5)
print("Texto 6: ", texto_6, "\n")


print("PARTE 2: ")
print("Una cadena")
print("Otra cadena")
print("Otra cadena mas", "\n")


print("PARTE 3: ")
print("Un texto\tuna tabulacion") # Tabulacion
print("Un texto\nNueva linea", "\n") # Salto de linea


print("PARTE 4: ")
print("C:\nombre\directorio")
print(r"C:\nombre\directorio", "\n") # Usando RAW mostramos en crudo


print("PARTE 5: ")
print("""Una linea
otra linea
otra linea\tuna tabulacion""", "\n")


print("PARTE 6: ")
c = "Esto es una cadena\ncon dos lineas"
print (c, "\n")


print("PARTE 7: ")
d= "Una cadena " "compuesta de dos cadenas"
print (d, "\n")


print("PARTE 8: ")
c1 = "Una cadena"
c2 = " otra cadena"
print(c1+c2, "\n")


print("PARTE 9: ")
diez_espacios = " " * 10
print(diez_espacios + "se han añadido 10 espacios.", "\n")