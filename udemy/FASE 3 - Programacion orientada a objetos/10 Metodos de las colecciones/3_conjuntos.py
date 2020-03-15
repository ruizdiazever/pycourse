# Metodo 1, sirve para descartar un elemento de un conjunto: .discard()
c = set()
c.add(1)
c.add(2)
c.add(3)
c.discard(2)
print("1.   ",c)

# Metodo 2, sirve para copiar el conjunto en otro: .copy()
c_2 = c.copy()
print("2.   ",c_2)
c.discard(1)
print("1.   ",c)
print("2.   ",c_2)

# Metodo 3, sirve para vaciar un conjunto: .clear()
c_2.clear()
print("3.   ",c_2)

# Metodo 4, es para saber si dos conjuntos son distintos totalmente en sus elementos: .isdisjoint()
conjunto_1 = {1,2,3}
conjunto_2 = {3,4,5}
conjunto_3 = {-1,99}
conjunto_4 = {1,2,3,4,5}
print("4.   ",conjunto_1.isdisjoint(conjunto_3)) # Son disjuntos? True, porque no concuerdan en ningun elemento.
print("4.   ",conjunto_1.isdisjoint(conjunto_2)) # Son disjuntos? False, porque concuendran en un elemento.

# Metodo 5, sirve para saber si un conjunto es un subconjunto de otro: .issubset()
print("5.   ", conjunto_1.issubset(conjunto_4))
print("5.   ", conjunto_4.issubset(conjunto_1)) # False, porque conjunto_1 no es un subconjunto del conjunto_1

# Metodo 6, sirve para saber si un conjunto contiene a otro conjunto: .issuperset()
print("6.   ", conjunto_4.issuperset(conjunto_1)) # True, porque contiene a otro conjunto.

# METODOS AVANZADOS
# Metodo 7, sirve para unir dos conjuntos: .union()
print("7.   ", conjunto_1.union(conjunto_2)) # Las une pero no la actualiza..
print("7.   ", conjunto_1)

# Metodo 8, sirve unir dos conjuntos y guarda en el primero: .update()
conjunto_1.update(conjunto_2)
print("8.   ", conjunto_1)

# Metodo 9, encuentra elementos distintos del primero conjunto de otro conjunto
c_1 = {1,2,3}
c_2 = {3,4,5}
c_3 = {-1,99}
c_4 = {1,2,3,4,5}
print("9.   ",c_1.difference(c_2)) # '1,2' de 'c_1' son elementos inexistentes en 'c_2'
print("9.   ",c_1)

# Metodo 10, lo mismo pero guarda y actualiza el primer conjunto
c_1.difference_update(c_2)
print("10.  ",c_1)

# Metodo 11, devuelve un conjunto con los elementos comunes:
c_98 = {55,30,77}
c_99 = {44,55,77}
print("11.  ", c_98.intersection(c_99))
print("11.  ", c_98, "Observacion: no se guardan.")
c_98.intersection_update(c_99) # De esta manera actualizamos el c_98
print("11.  ", c_98, "Observacion: se guardan.")

# Metodo 12, elimina los elementos iguales de los conjuntos, NO GUARDA
c_101 = {1,2,3}
c_102 = {3,4,5}
print("12.  ",c_101.symmetric_difference(c_102))
print("12.  ",c_101, "Observacion: NO GUARDA")


# Metodo 13, elimina los elementos iguales de los conjuntos, GUARDA
c_101.symmetric_difference_update(c_102)
print("13.  ",c_101, "Observacion: SI GUARDA")