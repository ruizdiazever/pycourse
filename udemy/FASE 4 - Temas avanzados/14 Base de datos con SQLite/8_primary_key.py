# Una clave primaria es un campo especial de una tabla que actúa 
    # como identificador único de los registros, en otras palabras, 
    # no se puede repetir un registro con la misma clave primaria. 
    # Por ejemplo dos usuarios con el mismo DNI.

import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()


# Creamos un campo dni como clave primaria
cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            dni VARCHAR(9) PRIMARY KEY,
            nombre VARCHAR(100), 
            edad INTEGER,
            email VARCHAR(100)
            )
            ''')

usuarios = [
            ('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('44444444D', 'Juan', 19, 'juan@ejemplo.com')
        ]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

conexion.commit()
conexion.close()