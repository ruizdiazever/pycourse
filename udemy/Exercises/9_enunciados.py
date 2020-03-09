# Hasta ahora sabemos que una clase heredada puede fácilmente extender algunas funcionalidades, simplemente añadiendo nuevos atributos y métodos, o sobreescribiendo los ya existentes. 
# Como en el siguiente ejemplo:
print("EJEMPLO 3:")
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)       
        
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada )
        
c = Coche("azul",4,250,1000)
print(c)



# El inconveniente más evidente de ir sobreescribiendo es que tenemos que volver a escribir el código de la superclase y luego el específico de la subclase.
# Para evitarnos escribir código innecesario, podemos utilizar un truco que consiste en llamar el método de la superclase y luego simplemente escribir el código de la clase:
print("\nEJEMPLO 2:")
class Vehiculo_2():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche_2(Vehiculo_2):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo_2.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada)

c_2 = Coche_2("rojo",4,350,1500)
print(c_2)



# Como tener que determinar constantemente la superclase puede ser fastidioso, Python nos permite utilizar un acceso directo mucho más cómodo llamada super().
# Hacerlo de esta forma además nos permite llamar cómodamente los métodos o atributos de la superclase sin necesidad de especificar el self.
print("\nEJEMPLO 3:")
class Vehiculo_3():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "El vehiculo {} tiene {} ruedas..".format(self.color,self.ruedas)
v = Vehiculo_3("negro mate",4)
print(v)

class Coche_3(Vehiculo_3):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "El vehiculo es de color {} con {} ruedas, posee {} de km/h de velocidad maxima y {} de cilindrada.".format(self.color,self.ruedas,self.velocidad,self.cilindrada)

auto_fantastico = Coche_3("rojo",4,475,2000)
print(auto_fantastico)



# Utilizando esta nueva técnica, extiende la clase Vehiculo y realiza la siguiente implementación: 
    # Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
    # Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
    # Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
    # También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
    # Recordatorio: Puedes utilizar el atributo especial de clase name de la siguiente forma para recuperar el nombre de la clase de un objeto:
    # type(objeto).__name__

print("\n\n\n\nEJEMPLO 4:")
class Vehiculo_4():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Vehiculo de color {} y {} ruedas.".format(self.color,self.ruedas)

class Coche_4(Vehiculo_4):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Vehiculo de color {}, {} ruedas, {} km/h de velocidad maxima y {} de cilindrada.".format(self.color, self.ruedas, self.velocidad, self.cilindrada)

# COMPLETA LOS EJERCICIOS AQUI:
# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
# Clases
class Camioneta(Coche_4):
    pass
class Bicicleta(Coche_4):
    pass
class Motocicleta(Coche_4):
    pass
# Objetos
camioneta = Camioneta("plateado",6,180,800)
bici = Bicicleta("negro con azul",2,35,None)
moto = Motocicleta("azul marino",2,190,350)

# Lista con objetos
vehiculos = [camioneta, bici, moto]

# Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
def catalogar(lista):
    for i in lista:
        print("ATRIBUTOS: ",i)
        print("NOMBRE DE SU CLASE:", type(i).__name__, "\n")
catalogar(vehiculos)

# Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento.
# También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
def catalogar_2(lista,ruedas):
    n = 0
    for i in lista:
        if i.ruedas == ruedas:
            n = n + 1
            print("- Resultado:\t",i)
        else:
            pass
    print("- Cantidad:\t Se han encontrado {} vehículos con {} ruedas.".format(n, ruedas))

catalogar_2(vehiculos,10)
    