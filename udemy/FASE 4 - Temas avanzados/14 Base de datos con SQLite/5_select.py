import sqlite3

conexion = sqlite3.connect('database.db')
cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Mostrar el cursos a ver que hay ?
print(cursor)

# Recorremos el primer registro con el método fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)
print(usuario[0])

conexion.commit()
conexion.close()