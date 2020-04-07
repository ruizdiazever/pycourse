# Esta función trabaja de una forma muy similar a filter(), 
# con la diferencia que en lugar de aplicar una condición a un 
# elemento de una lista o secuencia, aplica una función sobre 
# todos los elementos y como resultado se devuelve un iterable de tipo map:

numeros = [2,5,10,33,50,33]

def doblar(num):
    return num * 2

m = map(doblar, numeros) # (funcion, lista)
ml = list(map(doblar, numeros))

print("1.   ", m)
print("2.   ", ml)






# LAMBDA
ll = list(map(lambda x: x*2, numeros))
print("3.   ", ll)






# OTRO EJEMPLO
# La función map() se utiliza mucho junto a expresiones lambda ya que 
# permite ahorrarnos el esfuerzo de crear bucles for.

# Además se puede utilizar sobre más de un iterable con la condición 
# que tengan la misma longitud.

# Por ejemplo si queremos multiplicar los números de dos listas:

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

producto= list(map(lambda x, y: x*y, a,b))
print("4.   ", producto)







a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11,12,13,14,15]

producto = list(map(lambda x, y, h: x*y*h, a,b,c))
print("5    ", producto)








print("\n========== 6 =========")
class Persona:
    def __init__(self, name, edad):
        self.name = name
        self.edad = edad
    def __str__(self):
        return "{} de {} años.".format(self.name, self.edad)

personas = [
    Persona("Ever", 27),
    Persona("Valentina", 28),
    Persona("Hannah", 1),
    Persona("Bubu", 1)
]

def incrementar(persona):
    persona.edad += 1
    return persona

personas = map(incrementar, personas) # IMPORTANTEEEE

for persona in personas:
    print(persona)












# CON LAMBDA
print("\n========== 7 =========")
personas = [
    Persona("Ever", 27),
    Persona("Valentina", 28),
    Persona("Hannah", 1),
    Persona("Bubu", 1)
]

personas = map(lambda persona: Persona(persona.name, persona.edad+1), personas)
for persona in personas:
    print(persona)