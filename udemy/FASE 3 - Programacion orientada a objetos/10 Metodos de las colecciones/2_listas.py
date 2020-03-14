# Metodo 1, es para agregar un elemento al final de una lista: .append()
list_0 = [1,2,3,4,5]
list_0.append(6)
print("1.   ",list_0)

# Metodo 2, borra todos los elementos de una list: .clear()
list_0.clear() # vaciamos la list
print("2.   ",list_0) # despues mostramos

# Metodo 3, unir varias lists en una sola: .extend()
list_1 = [10,20,30]
list_2 = [40,50,60]
list_1.extend(list_2) # A la 'list_1' le extendemos la 'list_20'
print("3.   ",list_1)

# Metodo 4, permite contar cuantas veces aparece un elemento en una list: .count()
list_3 = [1,1,1,0,0,0,1,1,0]
print("4.   ",list_3.count(1))

# Metodo 5, permite encontrar el indice de un elemento: .index()
list_4 = ["Hannah","Valentina","Ever"]
list_5 = ["Hola","hola","hola"]
print("5.   ",list_4.index("Valentina"))
print("5.   ",list_5.index("hola")) # Discrimina mayusculas..

# Metodo 6, permite agregar un elemento en determinada posicion.. .insert()
list_6 = [1,2,3]
list_6.insert(0, "Hola") # posicion, elemento
print("6.   ",list_6)
list_7 = [5,10,15,25]
list_7.insert(-1,20) # en la penultima posicion añadimos '20'
print("6.   ",list_7)

# Metodo 7, elimina la ultima posicion o la posicion determinada: .pop()
list_8 = [10,20,30,40,50]
list_8.pop() # Aca elimina la ultima posicion
print("7.   ",list_8)
list_8.pop(1) # Eliminamos la posicion 1, osea '20'
print("7.   ",list_8)

# Metodo 8, elimina el elemento determinado: .remove()
list_9 = [10,"Hola","Adios"]
list_9.remove("Adios")
print("8.   ",list_9)
list_10 = [10,11,"Hola","Hola","hola"]
list_10.remove("Hola")
print("9.   ",list_10) # Solo elimina el primero

# Metodo 9, permite dar vuelta una lista: .reverse()
list_11 = [9,8,7,6,5,4,3,2,1,0]
list_11.reverse()
print("10.  ",list_11)
lista_12 = list("Hola mundo")
lista_12.reverse() #  Revertimos la lista
print("10.  ",lista_12)
cadena = "".join(lista_12)
print("10.  ",cadena)
cadena = list("EVER Y HANNAH")
cadena.reverse()
cadena = "".join(cadena)
print("10.  ",cadena)

# Metodo 10, permite ordenar una lista: .sort()
list_13 = [5,-5,8,-55,150,20]
list_13.sort()
print("11.  ",list_13)
list_14 = ['z','a','f','h','Z','B','T','A']
list_14.sort()
print("11.  ", list_14)
cadena_2 = [1,55,-5,1000,8]
cadena_2.sort(reverse=True) # Ordena alrevez
print("11.  ",cadena_2)