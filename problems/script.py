import pprint
import math

# Ejercicio 1.1
class Program:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hola {self.name}"
    
    def producto(self, num_1, num_2):
        print(f"{num_1} x {num_2} = {num_1 * num_2}")


# Ejercicio 1.2
class Geometria:
    def rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        print(f"Rectangulo con base {base} y altura {altura} || Perimetro: {2 * (base + altura)} || Area: {base * altura}")

    def rectangulo_coordenadas(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        diagonal = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(diagonal)

        print(f"x1={x1}, x2={x2}, y1={y1} y2={y2} => Area: {diagonal}")

    def circulo(self, radio):
        self.radio = radio
        print(f"Circulo de radio {radio} || Perimetro: {2 * math.pi * radio} || Area: {math.pi * (radio ** 2)}")

    def esfera(self, radio):
        self.radio = radio
        print(f"Esfera de radio {radio} || Volumen: {(4 * math.pi * (radio **3)) / 3}")       

    def triangulo_rectangulo(self, cateto_1, cateto_2):
        hipotenusa = math.sqrt((cateto_1 **2) + (cateto_2**2))
        print(f"Triangulo rectangulo, cateto 1= {cateto_1} cateto 2= {cateto_2} hipotenusa= {hipotenusa}")
