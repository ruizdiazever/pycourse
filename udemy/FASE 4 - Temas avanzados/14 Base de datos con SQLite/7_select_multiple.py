import sqlite3

conexion = sqlite3.connect('database.db')
cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Recorremos todos los registros con fetchall
# y los volcamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)

conexion.close()