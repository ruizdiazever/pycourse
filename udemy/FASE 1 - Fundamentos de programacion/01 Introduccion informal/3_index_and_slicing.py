palabra = "Python"

print("Posicion 0 de la cadena: ",palabra[0])
print("Posicion 3 de la cadena: ",palabra[3])
print("Posicion ultima de la cadena: ", palabra[-1], "\n")

print("Posicion 0 a 2: ",palabra[0:2]) # La ultima posicion se excluye, que seria "t"
print("Posicion 0 a 2: ",palabra[:2],"\n") # La ultima se excluye, que seria la "t"

print("Posicion 2 al penultimo: ",palabra[2:-1]) # La ultima posicion se excluye, que seria "n"
print("Posicion 2 al ultimo: ",palabra[2:],"\n")

print("Palabra de principio a final: ",palabra[:])
print("Palabra de principio a final: ", palabra[:2] + palabra[2:]+" (alternativo)", "\n")

print("Un ejemplo exotico: ", palabra[:99])
print("Otro ejemplo exotico: ", palabra[99:],"\n") # Esto no devuelve nada obviamente.

palabra_2 = palabra
palabra_2 = "N" + palabra_2[1:]
print("La palabra 2 es: ", palabra_2,"\n")
print("La cadena 'palabra_2' posee ",len(palabra_2), " caracteres") # Longitud de palabra_2