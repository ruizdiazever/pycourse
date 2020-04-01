import sqlite3

conexion = sqlite3.connect('database.db')
cursor = conexion.cursor()

# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO usuarios VALUES ('Ever', 27, 'ruizdiaz.oeq@gmail.com')")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()