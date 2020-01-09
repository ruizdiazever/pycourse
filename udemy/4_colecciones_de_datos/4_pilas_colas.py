# Pilas: una coleccion de elementos ordenados, permite dos acciones.
# Añadir o sacar, interesante es el ultimo en entrar es el primero en salir.

# Creamos una lista convencional
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)

# Sacar un ultimo elemento
pila.pop() # Borra el ultimo elemento de la lista

# Guardamos lo borrado en n
n = pila.pop()

# Mostramos
print(pila)
print(n)

# Borramos los 3 elementos de la lista
pila.pop()
pila.pop()
pila.pop()
print(pila) # Queda una lista vacia







# Cola: Coleccion donde el primer elemento en entrar es el primero en salir.
# Las colas se usan mucho en servidores.
from  collections import deque # Importamos esta libreria para cola

# Definos cola con deque() y mostramos
cola = deque()
print(cola)

# Llenamos una cola y mostramos
cola = deque(['Hector', 'Juan', 'Miguel'])
print(cola)

# Añadimos elementos a la cola
cola.append('Maria')
cola.append('Ronaldo')

# Guardamos los eliminados en una variable
eliminados = cola.popleft()

# Eliminamos elementos de una cola
cola.popleft()

# Mostramos eliminados
print("Eliminados: ", eliminados)

# Mostramos cola
print(cola) # Hector fue eliminado