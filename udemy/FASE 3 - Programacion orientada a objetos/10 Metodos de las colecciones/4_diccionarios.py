# Leccion 1, ejemplo de diccionario, repaso:
colores = {"amarillo":"yellow", "azul":"blue", "rojo":"red"}
print("1.   ", colores["amarillo"])

# Metodo que permite la busqueda por clave, con un segundo argumento en caso de no encontrarse: .get()
print("2.   ", colores.get("azul","No se encuentra"))
print("2.   ", colores.get("negro","No se encuentra"))

# Metodo que facilita saber si una clave se encuentra en un diccionario: True o False
print("3.   ", 'amarillo' in colores)
print("3.   ", 'negro' in colores)

# Metodo para devolver las claves del diccionario: .keys()
print("4.   ", colores.keys())

# Metodo para devolver los valores del diccionario: .values()
print("5.   ", colores.values())

# Metodo que muestras las claves y valores de un diccionario: .items()
print("6.   ", colores.items())
print("\n======== FOR KEYS ===========")
for c in colores.keys():
    print(c)
print("======== FOR VALUES ==========")
for c in colores.values():
    print(c)
print("======== FOR ITEMS ==========")
for c,v in colores.items():
    print(c,v)
print("=============================\n")

# Metodo para borrar por clave con un segundo argumento en caso de encontrarte
colores.pop('amarillo', 'No se ha encontrado.')
print("7.   ", colores)
print("7.   ", colores.pop('pink', 'No se ha encontrado'))

# Metodo para vaciar un diccionario
colores.clear()
print("8.   ", colores)