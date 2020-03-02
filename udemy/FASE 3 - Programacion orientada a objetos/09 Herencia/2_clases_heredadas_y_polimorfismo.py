# SUPERCLASE
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
Referencia:     {}
Nombre:         {}
PVP:            {}
Descripcion:    {}
""".format(self.referencia,self.nombre,self.pvp,self.descripcion)



# SUBCLASE
class Adorno(Producto):
    pass
adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")



# SUBCLASE
class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
Referencia:     {}
Nombre          {}
PVP:            {}
Descripcion:    {}
Productor:      {}
Distribuidor:   {}
""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)


# SUBCLASE
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
Referencia:     {}
Nombre          {}
PVP:            {}
Descripcion:    {}
Productor:      {}
Distribuidor:   {}
""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)



# CREAR OBJETOS Y DETERMINAR ATRIBUTOS
# ALIMENTO
alimento = Alimento(2077,"Avena integral",5,"Avena integral para cocinar o usar como harina")
alimento.productor = "Ever Molinos S.A."
alimento.distribuidor = "Ever Robotic S.A."
# LIBRO
libro = Libro(2036, "La Fundacion",9, "Clasico de la ciencia ficcion")
libro.isbn = "978-987-566-112-7"
libro.autor = "Isaac Asimov"



# TRABAJANDO EN CONJUNTO
print("TRABAJANDO EN CONJUNTO: \n")
    # Gracias a la flexibilidad de Python podemos manejar objetos de distintas clases masivamente de una forma muy simple.
    # Vamos a empezar creando una lista con nuestros tres productos de subclases distintas:

productos = [adorno, alimento]
productos.append(libro)

# Ahora si queremos recorrer todos los productos de la lista podemos usar un bucle for:
print("Recorremos todos los productos: ")
for producto in productos:
    print(producto, "\n")

# También podemos acceder a los atributos, siempre que sean compartidos entre todos los objetos:
print("Accedemos a los atributos, que son compartidos en todos los objetos:")
for producto in productos:
    print(producto.referencia, producto.nombre)

# Si un objeto no tiene el atributo al que queremos acceder nos dará error, ejemplo:
#for producto in productos:
#    print(producto.autor)

# Por suerte podemos hacer una comprobación con la función isinstance() para determinar si una instancia es de una determinado clase y así mostrar unos atributos u otros:
print("\nIterando con 'ininstance()':")
for producto in productos:
    if( isinstance(producto, Adorno) ): # Si el objeto 'producto' es del tipo Adorno, True
        print(producto.referencia, producto.nombre)
    elif( isinstance(producto, Alimento) ):
        print(producto.referencia, producto.nombre, producto.productor)
    elif( isinstance(producto, Libro) ):
        print(producto.referencia, producto.nombre, libro.isbn)  
# Esto tambien sirve para manipular los atributos unicos de los objetos.


# Funcion para rebajar precio de producto
# POLIMORFISMO DE CLASE: propiedad de la herencia en que objetos de distintas subclases pueden responder a una misma accion
# El metodo 'rebajar_producto()' recibe objetos de distintas clases y accede al atributo pvp dando por hecho que existe en ellos
# Si no lo tuviera daria ERROR
# En Python todas las clases son a su vez subclases de la superclase Object, es decir, son polimorficas por defecto
def rebajar_producto(p, rebaja):
    # Devuelve un producto con una rebaja en porcentaje de su precio
    p.pvp = p.pvp - (p.pvp/100*rebaja)
    return p

# Utilizamos la funcion
print("Utilizando funcion de rebaja:")
producto_rebajado = rebajar_producto(alimento,30)
print(producto_rebajado)
print("Comprobamos como queda 'alimento' despues de la funcion:")
print(alimento) # Tambien se rebaja porque se pasa como referencia, no por valor.


# Copiar un objeto, se utiliza un modulo externo llamado 'copy'
print("Copiando objetos, utilizando el modulo 'copy':")
import copy
copia_adorno = copy.copy(adorno)
print(copia_adorno)
copia_adorno.pvp = 50
print("COPIA ADORNO, con pvp cambiado:")
print(copia_adorno)
print("ADORNO ORIGINAL:")
print(adorno)
