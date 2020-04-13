# https://docs.hektorprofe.net/python/herencia-en-la-poo/ejercicios/

# 1) Utilizando esta nueva técnica extiende la clase Vehiculo y realiza la siguiente implementación:
    # Diagrama en el link arriba..

# Superclase
class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color: {}\nRuedas: {}".format(self.color, self.ruedas)

# Subclase 'Coche', hereda de la clase 'Vehiculo'
class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + "\nVelocidad maxima: {} km/h  \nCilindrada: {} cc".format(self.velocidad,self.cilindrada)

# Subclase 'Camioneta', hereda de la clase 'Coche'
class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga
    def __str__(self):
        return super().__str__(self) + "\nCarga maxima: {} kg".format(self.carga) # Una forma
        # return Coche.__str__(self) + "\nCarga maxima: {} kg".format(self.carga) # Otra forma

# Subclase 'Bicicleta', hereda de la clase 'Vehiculo'
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + "\nTipo: {}".format(self.tipo)

# Subclase 'Motocicicleta', hereda de la clase 'Bicicleta'
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + "\nVelocidad: {} km/h \nCilindrada: {} cc".format(self.velocidad,self.cilindrada)



# 2) Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos:
coche = Coche("rojo",4,235,650)
camion = Camioneta("negro",6,170,800,5000)
bici = Bicicleta("negro con azul",2,"deportiva")
moto = Motocicleta("gris",2,"urbana",195,350)
    # Lista 'vehiculos'
vehiculos = [coche, camion, bici, moto]
    # Funcion 'catalogar'
def catalogar(lista):
    for vehiculo in lista:
        print("{}".format(type(vehiculo).__name__.upper())) # upper() es para convertir en MAYUSCULAS
        #print(type(vehiculo).__name__.upper()) 
        print(vehiculo, "\n")
       



# 3) Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo 
    # que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
    # También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente 
    # si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
def catalogar(lista,ruedas):
    n = 0
    for vehiculo in lista:
        if vehiculo.ruedas == ruedas:
            print(type(vehiculo).__name__.upper()) # upper() es para convertir en MAYUSCULAS
            print(vehiculo, "\n")
            n = n + 1
        else:
            pass
    print("Se han encontrado {} vehiculos con {} ruedas.\n".format(n,ruedas))

# Version de profesor
def catalogar_2(lista,ruedas=None):

    if ruedas != None:
        contador = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
        print("Se han encontrado {} vehiculos con {} ruedas: ".format(contador,ruedas))
        print("===========================================")

    for vehiculo in lista:
        if ruedas == None:
            print("{} {}".format(type(vehiculo).__name__, vehiculo))
        else:
            if vehiculo.ruedas == ruedas:
                print("{} {}".format(type(vehiculo).__name__,vehiculo))
                print("======================")

catalogar(vehiculos,0)
catalogar_2(vehiculos,2)