# Superclass
class Vehiculo:
    def __init__(self,tipo,motor,velocidad_max,finalidad):
        self.tipo = tipo
        self.motor = motor
        self.velocidad_max = velocidad_max
        self.finalidad = finalidad
    def __str__(self):
        return """\
Tipo:               {}
Motor:              {}
Velocidad maxima:   {}
Finalidad:          {}
""".format(self.tipo,self.motor,self.velocidad_max,self.finalidad)

# Class Auto herededa de superclase Vehiculo
class Auto(Vehiculo):
    desplazamiento = ""
    descripcion = ""
    material = ""
    marca = ""
    modelo = ""

    def __str__(self):
        return """
Tipo:               {}
Motor:              {}
Velocidad maxima:   {}
Finalidad:          {}
Desplazamiento:     {}
Descripcion:        {}
Material:           {}
Marca:              {}
Modelo:             {}
""".format(self.tipo,self.motor,self.velocidad_max,self.finalidad,self.desplazamiento,self.descripcion,self.material,self.marca,self.modelo)        

auto = Auto("Automovil","Electrico","250 KM/H","Uso personal")
auto.desplazamiento = "Terrestre"
auto.descripcion = "Automovil con conduccion autonoma nivel 5, unica en su clase"
auto.marca = "Tesla"
auto.modelo = "Cybertruck"
auto.material = "Aluminio endurecida en frio"


# Class Avion heredada de superclase Vehiculo
class Avion(Vehiculo):
    desplazamiento = ""
    descripcion = ""
    altura_vuelo = ""
    fabricante = ""
    modelo = ""

    def __str__(self):
        return """ 
Tipo:               {}
Motor:              {}
Velocidad maxima:   {}
Finalidad:          {}
Desplazamiento:     {}
Altura maxima:      {}
Fabricante:         {}
Modelo:             {}        
""".format(self.tipo,self.motor,self.velocidad_max,self.finalidad,self.desplazamiento,self.altura_vuelo,self.fabricante,self.modelo)

avion = Avion("Aeronave","Reaccion","Cruzero","Transporte de pasajeros")
avion.altura_vuelo = "15 KM"
avion.fabricante = "Airbus"
avion.modelo = "A380"
avion.desplazamiento = "Aereo"

# Iteramos todos los objetos
vehiculos = [auto, avion]
for vehiculo in vehiculos:
    print("1. Tipo: ",vehiculo.tipo)

# Iteramos segun caracteristicas
for vehiculo in vehiculos:
    if (isinstance(vehiculo, Avion)):
        print("2. Desplazamiento: ",vehiculo.desplazamiento)
    elif (isinstance(vehiculo, Auto)):
        print("3. Marca: ",vehiculo.marca)
