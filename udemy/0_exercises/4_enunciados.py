# 1) Realiza un programa que siga las siguientes instrucciones:
        # A) Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
        # B) Crea un conjunto llamado administradores con los administradores Juan y Marta.
        # C) Borra al administrador Juan del conjunto de administradores.
        # D) Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
        # E) Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
        # F) Notas: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.


# Exercise 1
usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'} # A
administradores = {'Juan','Marta'} # B
administradores.discard('Juan') # C
print(administradores)
administradores.add('Marcos') # D
print(administradores)
for persona in usuarios:
        if persona in administradores:
                print(persona, "es administrador.")
        else:
                print(persona, "no es administador")


# 2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:
        # A) El caballero tiene el doble de vida y defensa que un guerrero.
        # B) El guerrero tiene el doble de ataque y alcance que un caballero.
        # C) El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
        # D) Muestra como quedan las propiedades de los tres personajes.
print("\n","\tEXERCISE 2")
caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

# A
caballero['vida'] = guerrero['vida']*2
caballero['defensa'] = guerrero['defensa']*2
# B
guerrero['ataque'] = caballero['ataque']*2
guerrero['alcance'] = caballero['alcance']*2
# C
arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] *2
# D
personajes = []
personajes.append(caballero)
personajes.append(guerrero)
personajes.append(arquero)
print("CABALLERO: ")
for clave, valor in caballero.items():
        print(clave, valor)
print("\n")
print("GUERRERO: ")
for clave, valor in guerrero.items():
        print(clave, valor)
print("\n")
print("ARQUERO: ")
for clave, valor in arquero.items():
        print(clave, valor)
# D (alternativa)
print("Caballero:\t",caballero)
print("Caballero:\t",guerrero)
print("Caballero:\t",arquero)




# 3) Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
                # ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
                # Pista: Para ordenar automáticamente una lista es posible utilizar el método .sort().
from  collections import deque

# Esto por cierto son las etapas de un videojuego
print("\n", "\tEXERCISE 3")
tareas = [ 
[6, 'Distribución'],
[2, 'Diseño'],
[1, 'Concepción'],
[7, 'Mantenimiento'],
[4, 'Producción'],
[3, 'Planificación'],
[5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
        print(tarea[0], tarea[1])

print("==Tareas ordenadas==")
tareas.sort()
for tarea in tareas:
        print(tarea[0], tarea[1])

cola = deque() # Creamos cola

for tarea in tareas:
        cola.append(tarea[1])
print(cola)

