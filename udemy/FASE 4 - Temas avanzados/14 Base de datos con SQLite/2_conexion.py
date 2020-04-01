# https://docs.hektorprofe.net/python/bases-de-datos-sqlite/consultas-sql-basicas/

# Importamos el módulo
import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('database.db')

# Cerramos la conexión, si no la cerramos quedará abierta
# y no podremos gestionar el fichero
conexion.close()