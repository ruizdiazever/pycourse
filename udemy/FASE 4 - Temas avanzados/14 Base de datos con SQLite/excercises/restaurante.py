import sqlite3

def crear_bd():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()
    # TABLA CATEGORIA
    try:
        cursor.execute('''
            CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("Tabla | Categoria => ya ha sido creada.")
    else:
        print("Tabla | Categoria => creada exitosamente")
    # TABLA PLATO
    try:
        cursor.execute('''
            CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("=====================================================")
        print("Tabla | Plato => la tabla ya ha sido creada.")
    else:
        print("=====================================================")
        print("Tabla | Plato => creada exitosamente.")

    conexion.commit()
    conexion.close()



def agregar_categoria():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    while(True):
        try:
            print("=====================================================")
            name_category = str(input("Ingrese nombre para categoria: "))
        except Exception as e:
            print("Error, introduzca el nombre nuevamente: ", type(e).__name__)
        else:
            print("{} => categoria introducido correctamente.".format(name_category))
            break
    
    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(name_category))
    except sqlite3.OperationalError:
        print("Categoria | {} => la tabla ya ha sido creada.".format(name_category))
    except sqlite3.IntegrityError:
        print("Categoria | {} => la tabla ya ha sido creada.".format(name_category))
    except Exception as e:
        print("ERROR!   ", type(e).__name__)
    else:
        print("Categoria => {} => creada exitosamente.".format(name_category))
    
    conexion.commit()
    conexion.close()



def mini_menu():
    try:
        while(True):
            print("=====================================================")
            print("""BIENVENIDO, ¿Que desea hacer?
1) Crear categoria.
2) Salir.""")
            print("=====================================================")
            num = int(input("Introduzca: "))

            if num == 1:
                agregar_categoria()
            else:
                break
    except Exception as e:
        print("Error! Opcion invalida!", type(e).__name__)


def agregar_plato():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    print("=====================================================")
    print("Categorias disponiblesm elija una opcion: ")
    for categoria in categorias:
        print("{}) {}".format(categoria[0], categoria[1]))
    
    id_input = int(input("\n> "))
    print("=====================================================")

    # Platos
    primeros = "Ensalada del tiempo + zumo de tomate." # 1
    segundos = "Estofado de pescado o Pollo con patatas." # 2 
    postres = "Flan con nata o Fruta de temporada." # 3

    # Obtenemos valores
    primeros_id = categorias[0][0]
    segundos_id = categorias[1][0]        
    postre_id = categorias[2][0]

    # Casteamos
    primero_id = int(primeros_id)
    segundo_id = int(segundos_id)
    postre_id = int(postre_id)
    
    platito = ""
    try:
        if id_input == primero_id:
            platito = primeros
        elif id_input == segundos_id:
            platito = segundos
        elif id_input == postre_id:
            platito = postres
        else:
            print("Incorrecto, intentelo mas tarde nuevamente!")
            pass
    except Exception as e:
        print("ERROR! ", type(e).__name__)

    while id_input == primero_id or id_input == segundos_id or id_input == postre_id:
        try:
            cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(platito, id_input))
        except Exception as e:
            print("ERROR!", type(e).__name__)
    else:
        pass

    conexion.commit()
    conexion.close()



def mostrar_menu():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    menu = cursor.execute("SELECT * FROM plato").fetchall()
    
    print("1. Menu: {}".format(menu[0][1]))
    print("2. Menu: {}".format(menu[1][1]))
    print("3. Menu: {}".format(menu[2][1]))





#crear_bd()
#agregar_categoria()
#mini_menu()
#agregar_plato()
mostrar_menu()