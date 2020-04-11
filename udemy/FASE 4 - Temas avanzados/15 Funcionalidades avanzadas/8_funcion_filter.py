# Tal como su nombre indica filter significa filtrar, y es una de mis 
# funciones favoritas, ya que a partir de una lista o iterador y una función 
# condicional, es capaz de devolver una nueva colección con los elementos 
# filtrados que cumplan la condición.

# Por ejemplo, supongamos que tenemos una lista varios números y queremos 
# filtrarla, quedándonos únicamente con los múltiples de 5...


numeros = [2, 5, 10, 23, 50, 33]
def multiple(numero):
    if numero % 5 == 0:
        return True

f = filter(multiple, numeros) # Condicion, elementos

# Iteramos con next()
print(next(f))
print(next(f))
print(next(f))

# Convertimos en lista
print(list(f))



# LAMBDA
lista = list(filter(lambda num: num % 5 == 0, numeros))
print(lista)


# FILTER CON OBJETOS
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

# Creamos una lista con onjetos Persona
personas = [
    Persona("Ever",27),
    Persona("Valentina", 28),
    Persona("Hannah", 1),
    Persona("Bubu", 1)
]

# Funcion lambda con filter
menores = filter(lambda persona: persona.edad < 18, personas)

# Menores
for menor in menores:
    print(menor)