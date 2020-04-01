import sqlite3

conexion = sqlite3.connect("database.db")

cursor = conexion.cursor()

# Creamos una lista con varios usuarios
usuarios = [
    ('Valentina',28,'valen@gmail.com'),
    ('Hannah',1,'hannah@gmail.com'),
    ('Mario',31,'mario@gmail.com'),
]

# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

conexion.commit()
conexion.close()