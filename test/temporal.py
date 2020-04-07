def example(number):
    print("\n========================== {} ==========================".format(number))


example(1)
lista = [numero for numero in [numero**2 for numero in range (0,11)] if numero % 2 == 0]
print(lista)


example(2)
import pprint
lista = [1,2,3,4]
name = ["Ever", "Hannah", "Valentina", "Familia"]
lista_3 = []
for i in name:
    for l in lista:
        lista_3.append(l*i)
pprint.pprint(lista_3)

example(3)
# comprimir lista anterior
reduccion = list(map(lambda x,y: x*y, lista,name))
print(reduccion)

example(3.1)
lista = [(lista, name) for lista in name]
print(lista)


example(4)
class Persona():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __str__(self):
        return """USER: {}
EMAIL: {}""".format(self.name,self.email)

p = Persona("Ever","ruizdiaz.oe@gmail.com")
print(p)