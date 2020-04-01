import sqlite3
import pprint

# Una vez contamos con algún campo que nos sirva de identificador único, 
# podemos realizar consultas específicas utilizando la cláusula WHERE:

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

# Recuperamos un registro de la tabla de usuarios
#cursor.execute("SELECT * FROM usuarios WHERE id=1")
cursor.execute("SELECT * FROM usuarios WHERE edad=27")
# Con DNI
#cursor.execute("SELECT nombre, edad, email FROM usuarios WHERE dni='22222222B'")

""" usuario = cursor.fetchone()
print(usuario) """

usuarios = cursor.fetchall()
print(usuarios)

for user in usuarios:
    pprint.pprint(user)

conexion.close()