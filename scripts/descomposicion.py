import sys

if len(sys.argv) == 2:
	numero = int(sys.argv[1])
	if numero < 0 or numero > 9999:
		print("Error - Número es incorrecto")
		print("Ejemplo: descomposicion.py [0-9999]")
	else:
		# Aqui va la lógica
		cadena = str(numero)
		longitud = len(cadena)

		for i in range(longitud):
			print( "{:04d}".format(int(cadena[longitud-1-i]) * 10 ** i ))
            # Longitud ejemplo 4 de 5780
            # 4 -1 - i(0) = 3
            # 4 -1 - i(1) = 2 penultimo caracter
            # 4 -1 - i(2) = 1

            # El truco para iterar al reves es -1-i

else:
	print("Error - Argumentos incorrectos")
	print("Ejemplo: descomposicion.py [0-9999]")