# Capacidad de una clase de heredar atributos y metodos de otra.
# Ademas de agregar nuevos o modificar los heredados.
# Relacion Superclase > subclase


# SIN HERENCIA: INEFICIENTE

# class Producto: 
    #def __init__(self,referencia,tipo,nombre,pvp,descripcion,productor=None,distribuidor=None,isbn=None,autor=None):
        #self.referencia = referencia
        #self.tipo = tipo
        #self.nombre = nombre
        #self.pvp = pvp
        #self.descripcion = descripcion
        #self.productor = productor
        #self.distribuidor = distribuidor
        #self.isbn = isbn
        #self.autor = autor
    
#adorno = Producto('000A','ADORNO','Vaso adornado',15,'Vaso de porcelana con dibujos')

# Para consultas
#print(adorno.tipo)          # Tipo
#print(adorno.pvp)           # Precio de venta al publico
#print(adorno.descripcion)   # Descripcion




# CON HERENCIA:
# 1. SUPERCLASE
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    def __str__(self):
        # Con diagonal le indicanos que no comience con espacio.
        # Dejando lo demas a la izquierda indicamos la posicion.
        return """\
REFERENCIA:   {}
NOMBRE:       {}
PVP:          {}
DESCRIPCION:  {}
        """.format(self.referencia,self.nombre,self.pvp,self.descripcion)




# 2. SUBCLASE SIN ATRIBUTOS EXTRAS
class Adorno(Producto):
    pass
a = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con arboles")
print(a)




# 3. SUBCLASE CON ATRIBUTOS NUEVOS, con asignacion externa.
class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA:   {}
NOMBRE:       {}
PVP:          {}
DESCRIPCION:  {}
PRODUCTOR:    {}
DISTRIBUIDOR: {}
        """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

al = Alimento(2035,"Leche descremada",5,"250ml en envase de vidrio.")
al.productor = "La Serenisima"
al.distribuidor = "Logistica Tesla SA"
print(al)

# 4. SUBCLASE CON ATRIBUTOS NUEVOS, con asignacion externa.
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA:   {}
NOMBRE:       {}
PVP:          {}
DESCRIPCION:  {}
ISBN:         {}
AUTOR:        {}
        """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)

li = Libro(2077,"La Fundacion",5,"Saga emblematica de la ciencia ficcion.")
li.isbn = "978-987-566-112-7"
li.autor = "Isaac Asimov"
print(li)