# Son colecciones desordenadas de elementos unicos, se utilizan normalmente
# para hacer pruebas de pertenencia a grupos y de eliminacion
# de elementos duplicados, soporta operaciones matematicas avanzadas

# Conjunto vacio
conjunto = set()
print("1. ",conjunto)

# Conjunto con varios elementos
conjunto_2 = {1,2,3}
print("2. ",conjunto_2)

# Metodo .add
conjunto_2.add(4)
conjunto_2.add(0)
print("3. ",conjunto_2)

# Agregamos un string
conjunto_2.add("H")
conjunto_2.add("A")
conjunto_2.add("Z")
print("4. ",conjunto_2)

# Grupo de personas
grupo = {'Ever','Valentina','Sofia'}
print('Ever' in grupo) # Devuelve True
print('Pepe' in grupo) # Devuelve False
print('Maria' not in grupo) # Devuelve True

# No pueden haber elementos repetidos
test = {'Ever','Ever','Hannah'}
print("6. ", test)

# Eliminar elementos repetidos de una lista
lista = [1,2,3,4,3,2,4,1]
conjunto_3 = set(lista) # Convertimos lista a conjunto
lista = list(conjunto_3)
print("7. ", lista)

# Conversion en una linea
l = [1,2,3,3,2,1]
l = list( set(l) )
print("8. ", l)
l_2 = 'Al pan pan y al vino vino' # Elimina letras repetidas
l_2 = list(set(l_2))
print("8. ", l_2)

