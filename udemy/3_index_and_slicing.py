palabra = "Python"

print("Posicion 0 de la cadena: ",palabra[0])
print("Posicion 3 de la cadena: ",palabra[3])
print("Posicion ultima de la cadena: ", palabra[-1], "\n")

print("Posicion 0 a 2: ",palabra[0:2]) # La ultima posicion se excluye, que seria "t"
print("Posicion 0 a 2: ",palabra[:2],"\n") # La ultima se excluye, que seria la "t"

print("Posicion 2 al penultimo: ",palabra[2:-1]) # La ultima posicion se excluye, que seria "n"
print("Posicion 2 al ultimo: ",palabra[2:],"\n")