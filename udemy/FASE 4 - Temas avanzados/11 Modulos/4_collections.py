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
print(diccio['algo']) # Da error porque esta clave no existe..