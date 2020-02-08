# Las tuplas a diferencia de listas son inmutables

tuplas = (100,"Hola",[1,2,3,4],-50) # La lista no se podra modificar.

print("1] ",tuplas)
print("2] ",tuplas[0]) # Primer elemento
print("3] ",tuplas[-1]) # Ultimo elemento
print("4] ",tuplas[0:]) # Primero a final
print("5] ",tuplas[2][2]) # Accedemos dentro de la lista
print("6] ",len(tuplas)) # Longitud de tupla
print("7] ",len(tuplas[2])) # Longitud de lista en tupla

# .index para buscar un elemento y saber su posicion
print("8] ",tuplas.index("Hola"))

# .count
print("9] ",tuplas.count(100))
print("10] ",tuplas.count("Algo"))
