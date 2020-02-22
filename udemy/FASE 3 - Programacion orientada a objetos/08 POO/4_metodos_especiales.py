def salto(num):
    print("\nEJEMPLO",num,":")




# EJEMPLO 1: mostrar objeto en crudo.
salto(1)
class Serie:
    # Constructor de la clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
s = Serie("Mr. Robot","4 Temporadas","2015")
print(s)    
#           <__main__.Serie object at 0x0000011CCC3754C0>
#           Referencia a una instancia de tipo Serie que esta almacenada en la memoria (el codigo).





# EJEMPLO 2: Constructor, destructor y redefinir STRING.
salto(2)
class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)
    # Destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula",self.titulo)
    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos.".format(self.titulo,self.lanzamiento,self.duracion)
p = Pelicula("El Padrino",175,1972)
print(str(p))
del(p) # Destruimos la instancia





# EJEMPLO 3: test personal.
salto(3)
class Serie_2:
    # Constructor de la clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
    def __str__(self):
        return "{} posee {} y su primer episodio fue lanzado en {}.".format(self.titulo,self.duracion,self.lanzamiento)
s2 = Serie_2("Mr. Robot","4 Temporadas","2015")
print(s2)



# EJEMPLO 4: metodo len
salto(4)
class Pelicula_2:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)
    # Destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula",self.titulo)
    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos.".format(self.titulo,self.lanzamiento,self.duracion)
    # Redefinimos el metodo LENGTH
    def __len__(self):
        return self.duracion
p_2 = Pelicula_2("El Padrino",175,1972)
print(len(p_2)) # Aca mostramos la duracion de la pelicula. La definimos en len.
