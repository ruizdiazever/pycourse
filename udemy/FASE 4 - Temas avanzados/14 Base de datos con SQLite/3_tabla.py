# https://docs.hektorprofe.net/python/bases-de-datos-sqlite/consultas-sql-basicas/

import sqlite3 # Importamos el módulo
conexion = sqlite3.connect('database.db')# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios con nombres, edades y emails
cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close() # Cerramos la conexión, si no la cerramos quedará abierta y no podremos gestionar el fichero