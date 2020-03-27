from io import open
import pickle

class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return # para que salga de la posicion
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+') # 'ab+' es lectura y escritura binaria
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()

    # Destructor de clase
    def __del__(self):
        self.guardar() # guardado automatico
        print("Se ha guardado el fichero")

print("0.  ")
c = Catalogo()
c.mostrar()

print("\n1. ")
c.agregar(Pelicula("El Padrino",175,1972))
c.agregar(Pelicula("El Padrino: Parte 2",202,1994))

print("\n2. ")
c.mostrar()
del(c)

print("\n3. ")
c = Catalogo()
c.mostrar()

print("\n4. ")
c.agregar(Pelicula("Prueba",200,2019))
c.mostrar()

print("\n5. ")
c = Catalogo()