import pickle
import sys
sys.path.insert(1,'D:/Personal/Google Drive/dev/technologies/python/programs')
from examples import ejemplo


lista_num = [1,2,3,4,5]


ejemplo(1)
fichero = open('lista.pckl', 'wb') # 'wb' es escritura binario
pickle.dump(lista_num, fichero) # Metodo que sobreescribe, (valores, fichero)
fichero.close()


ejemplo(2)
fichero = open('lista.pckl', 'rb') # 'rb' es lectura binaria
lista_num = pickle.load(fichero) # Carga el fichero que indiquemos
print(lista_num)


ejemplo(3)
fichero.seek(0)
lista_num = pickle.load(fichero)
print(lista_num)
fichero.close()


ejemplo(4)
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

nombres = ["Hannah", "Ever", "Valentina"]
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)

fichero = open('personas.pckl', 'wb')
pickle.dump(personas, fichero)
fichero.close()

fichero = open('personas.pckl', 'rb')
personas = pickle.load(fichero)
fichero.close()

for p in personas:
    print(p)