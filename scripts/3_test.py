import sys # Importamos sys
texto = sys.argv[1] # Asignamos a texto el primer argumento
repeticiones = int(sys.argv[2]) # Tomamos el segundo argumento como repeticiones

for r in range(repeticiones):
    print(texto)


# Cuando ejecutemos este Script en la terminal va a ejecutar el primer argumento la cantidad
# que declaramos en el segundo argumento, el cual tendria que haber sido un numero.
# IMPORTANTE: los argumentos siempre se toman como cadenas