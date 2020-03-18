# PRIMERA LECCION: counter o contador, subclase del diccionario que nos ayuda a contar objetos..
# Tambien cuantas veces se re repite un elemento
from collections import Counter

lista = [1,2,3,4,1,2,3,1,2,1]
print("1.0  ", Counter(lista))

lista_2 = ["ever","lala","ever","Ever"]
print("1.1  ", Counter(lista_2))

cadena = "Hannah"
print("1.2  ", Counter(cadena))

animales = "gato perro canario perro canario perro"
print("1.3  ", Counter(animales))

print("1.4  ", Counter(animales.split(" "))) # este metodo separa en una lista una cadena por el caracter elegido..

# Uno de los mas utiles: nos muestra el o los  elementos mas comunes
# Si no ingresamos valor nos muestra todos los resultados
c = Counter(animales.split(" "))
print("1.5  ", c.most_common(1))

lista_3 = [10,20,30,40,10,20,30,10,20,10]
b = Counter(lista_3)
print("1.6  ", b)
print("1.7  ", b.items()) # Clave, valor
print("1.8  ", b.keys()) # Clave
print("1.9  ", b.values()) # Valor
print("1.10 ", sum(b.values()))
print("1.11 ", list(b))
print("1.12 ", dict(b))

d = dict(b)
#print("1.13 ",d.most_common(1)) # No funciona, porque ahora es un diccionario normal.


# SEGUNDA LECCION: si buscamos encontrar un valor y que nunca de error a pesar no encontrarse.
diccio = {}
#print(diccio['algo']) # Ejemplo, da error porque esta clave no existe..

from collections import defaultdict # Con esto lo solucionamos

print("\nEjemplo de 'defaultdict' con 'float' como tipo por defecto:")
diccio_2 = defaultdict(float) # Hay que indicarle un tipo por defecto
print("2.0   ", diccio_2['algo']) # 'algo' es nuestra clave de prueba
print("2.0  ", diccio_2)

print("\nEjemplo de 'defaultdict' con 'str' como tipo por defecto:")
diccio_2 = defaultdict(str) # Aca le indicamos un string como tipo por defecto
print("2.3   ", diccio_2['algo'])
print("2.3  ", diccio_2)

print("\nEjemplo de 'defaultdict' con 'object' como tipo por defecto:")
diccio_2 = defaultdict(object) # Aca le indicamos un object (clase padre de todo) como tipo por defecto
print("2.4  ", diccio_2['algo'])
print("2.4  ", diccio_2)

print("\nEjemplo de 'defaultdict' con 'int' como tipo por defecto:")
diccio_2 = defaultdict(int) # Entero
diccio_2['algo'] = 2.1
print("2.5  ", diccio_2['algo']) # Clave por defecto no afecta
print("2.6  ", diccio_2['algomas'])

# Los diccionarios son colecciones desordenadas..
print("\nLos diccionarios son colecciones desordenadas: ")
n = {}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'thee'
print("3.   ", n) # Generalmente se muestra en un orden aleatorio

# Esto permite ordenar el diccionario en el orden que nosotros le vamos agregando elementos
print("\nCon 'OrderedDict de 'collection' logramos ordenar un diccionario en el orden de agragacion:")
from collections import OrderedDict
n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'thee'
print("4.   ", n)
# Ejemplo de diccionario convencional
n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'
n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'
print("4.1  ", n1 == n2) # True
# Ejemplo de diccionario con ordererdict
n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'
n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'
print("4.1  ", n1 == n2) # False, se tiene en cuenta el orden

# ULTIMA LECCION, TUPLAS:
print("\nULTIMA LECCION, TUPLAS:")
t = (20,40,60)
print("5.0  ", t[-1])

# A veces nos interesa crear una estructura inmutable con distintos campos:
# Es una forma sencilla de guardar informacion inmutable.
from collections import namedtuple # importamos
Persona = namedtuple('Persona','nombre apellido edad') # Esto es una tupla con nombre
p = Persona(nombre='Ever', apellido='Ruiz Diaz', edad='27')
print("5.1  ",p)
print("5.2  ",p.apellido)
print("5.2  ",p[-1])