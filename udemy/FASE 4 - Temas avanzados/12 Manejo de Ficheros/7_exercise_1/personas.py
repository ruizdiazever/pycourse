# Importamos modulos necesarios
import pickle
import sys

# Lista y diccionario
personas = []

# Leemos fichero
fichero = open('personas.txt', 'r', encoding="utf8")
lineas = fichero.readlines()
fichero.seek(0)
fichero.close()
#print(lineas)

for linea in lineas:
    linea_2 = linea.replace("\n","").split(";")
    persona = {"id":linea_2[0], "nombre":linea_2[1], "apellido":linea_2[2], "nacimiento":linea_2[3]}
    personas.append(persona)

for p in personas:
    print("(id={}) {} {} => {}".format(p['id'], p['nombre'], p['apellido'], p['nacimiento']))

