# Son junto a las listas las colecciones mas usadas en Python
# 'clave':'valor'

# Example
vacio = {}
print(vacio)
print(type(vacio))

# Example
colores = {'amarillo':'yellow','azul':'blue', 'verde':'green'}
print(colores)
print(colores['azul'])

# Key with number
numeros = {10:'diez', 20:'veinte'}
print(numeros[10])

# Cambiamos valor de clave
colores['amarillo'] = 'white'
print(colores['amarillo'])

# Borrar clave y su valor
del(colores['amarillo'])
print(colores)

# Example
edades = {'Ever':26, 'Valentina':28, 'Hannah':1}
print(edades)

# Cambiar edad de Ever
edades['Ever'] = 27
print(edades)

# Cambiar de nuevo edad de Ever
edades['Ever'] += 1
print(edades)

# Sumar edades
print(edades['Ever']+edades['Valentina'])

# Recorrer todos los elementos de un diccionario con un FOR
for edad in edades:
    print(edad) # Asi accedemos a las claves

for clave in edades:
    print(edades[clave]) # Asi accedemos a los valores

for clave in edades:
    print(clave, edades[clave]) # Asi mostramos ambos valores

# Metodo .item
for clave, valor in edades.items():
    print(clave,valor)

# Conjunto con listas (Ejemplo lista de personajes)
personajes = []
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
personajes.append(p) # Una lista con un diccionario
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)

# Usamos un FOR para mostrarlo
print(personajes)
for p in personajes:
    print(p['Nombre'],p['Clase'],p['Raza'])