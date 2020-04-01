import sqlite3

conexion = sqlite3.connect("productos.db")

cursor = conexion.cursor()

# Al utilizar un nuevo campo autoincremental, la sintaxis sencilla para insertar 
# registros ya no funciona, pues en primer lugar se espera un identificador único, 
# por lo que recibimos un error indicándonos se esperan 4 columnas en lugar de 3:

electronica = [
            ("Teclado", "Logitech", 19.95),
            ("Pantalla 19", "LG", 89.95),
            ("Altavoces 2.1","LG", 24.95),
            ]

# Para arreglarlo cambiaremos la notación durante la inserción, especificando el valor null para el auto incremento:
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", electronica)

conexion.commit()
conexion.close()