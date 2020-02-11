class Pelicula:
    # Constructor de la clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula: ',self.titulo)
    # Redefinimos string
    def __str__(self):
        return "{} ({})".format(self.titulo,self.lanzamiento)

class Catalogo:
    peliculas = []
    def __init__(self,peliculas=[]):
        self.peliculas = peliculas
    def agregar (self,p):
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)

p1 = Pelicula("El Padrino",175,1972) # Pelicula 1
c1 = Catalogo([p1]) # Catalogo 1, IMPORTANTE! como agregar un objeto a la lista.
c1.mostrar()
c1.agregar(Pelicula("El Padrino: Parte 2",202,1974))
c1.mostrar()

# Probar borrar peliculas, modificarlas, ordenarlas por nombre, por año, etc.