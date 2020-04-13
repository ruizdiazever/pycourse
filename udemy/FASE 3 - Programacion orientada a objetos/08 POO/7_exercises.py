import math

# Ejercicio en https://docs.hektorprofe.net/python/programacion-orientada-a-objetos/ejercicios/

class Punto:
    # Constructor
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x,self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self)) # Con self le pasamos el propio objeto.
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} pertenece al punto de origen".format(self))
    
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y))

    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los dos {} y {} es {}".format(self,p,d))

class Rectangulo:
    def __init__(self,pInicial=Punto(),pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x) # valor absoluto por si es negativo
        print("La base del rectangulo es {}".format(self.base))

    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)  
        print("La altura del rectangulo es {}".format(self.altura))
        
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y) 
        self.area = self.base * self.altura
        print("El area del rectangulo es {}".format(self.area))


# A(2, 3), B(5,5), C(-3, -1) y D(0,0)
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)
# Consulta a que cuadrante pertenecen el punto A, C y D.
print("CUADRANTES")
A.cuadrante()
C.cuadrante()
D.cuadrante()
# Consulta los vectores AB y BA.
print("VECTORES")
A.vector(B)
B.vector(A)
# Consulta la distancia entre los puntos 'A y B' y 'B y A'.
print("DISTANCIAS")
A.distancia(B)
B.distancia(A)
print("DISTANCIA DEL PUNTO DE ORIGEN")
# Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)
A.distancia(Punto(0,0))
B.distancia(D)
C.distancia(D)
# Rectangulos
print("RECTANGULOS")
R = Rectangulo(A,B)
R.base()
R.altura()
R.area()

