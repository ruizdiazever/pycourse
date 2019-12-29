number = [1,2,3,4]
datos = [4, "Una cadena", -15, 3.14, "Otra cadena"] # Python acepta una lista con distintos tipos de dato.

print("Posicion 3: ",datos[3])
print("Ultima posicion: ",datos[-1])
print("Desde el penultimo al final: ", datos[-2:])


# CONCATENAR LISTAS
number = number + [5,6,7,8]
print ("Concatenado: ",number)

# REEMPLAZAR
pares = [0,2,4,5,8,10]
pares[3]= 6
pares.append(12) # Metodo APPEND, agrega un elemento al final de la lista
pares.append(7*2)
print("Pares: ",pares)

# OTRA LISTA
letters = ['a','b','c','d','e','f']
letters[:3] = ['A','B','C']
print("Letras: ", letters)

# VACIAR LISTA
letters_2 = letters # Aca referenciamos (NO SE CLONA)
letters_2[:3] = []
print("Lista vaciada: ", letters_2)

# LONGITUD
print("Longitud de letters: ",len(letters))
print("Elementos de letters: ",letters)

# LISTAS ANIDADAS
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print("Lista anidada: ", r)
print("Ultima posicion de lista anidada: ",r[-1]) # [7,8,9]
print("Primer elemento de la primera lista: ",r[0][0]) # 1
print("Penultimo elemento de la segunda lista: ", r[1][-2]) # 5