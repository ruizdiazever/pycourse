# Capacidad de una clase de heredar atributos y metodos de otra.
# Ademas de agregar nuevos o modificar los heredados.
# Relacion Superclase > subclase


class Producto:
    def __init__(self,referencia,tipo,nombre,pvp,descripcion,productor=None,distribuidor=None,isbn=None,autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor
    
adorno = Producto('000A','ADORNO','Vaso adornado',15,'Vaso de porcelana con dibujos')

# Para consultas
print(adorno.tipo)          # Tipo
print(adorno.pvp)           # Precio de venta al publico
print(adorno.descripcion)   # Descripcion