# Necesario para abrir ficheros desde un script
from io import open
from os import remove

texto = "Una linea con texto\nOtra linea de texto\nHola Ever"


# Fichero de trabjo y modo escritura 'w'
fichero = open('fichero.txt','w') # Si esto ya existe, lo borra y crear uno nuevo..
fichero.write(texto) # Metodo escribir
fichero.close() # Metodo close, necesario para guardar los cambios
#remove("fichero.txt") # Metodo para borrar archivos


# Fichero de trabjo y modo lectura 'r'
fichero = open('fichero.txt','r')
texto = fichero.read() # Guardamos todo el contenido de fichero en texto..
fichero.close() # Importante siempre cerrarlo
print(texto)


fichero = open('fichero.txt','r')
lineas = fichero.readlines() # Leer lineas, los guarda en lista..
fichero.close()
print(lineas)
print(lineas[1])
print(lineas[-1])


# 'a' se abre en modo append (extension)
# Con este modo se escribe al fina del todo..
fichero = open('fichero.txt','a')
fichero.write('\nCuarta linea del fichero')
fichero.close()


# No se pueden abrir ficheros inexistentes
#fichero = open('fichero_inexistente.txt', 'r')


# En cambio en modo append si funciona
# Lo crea vacio
fichero = open('fichero_inexistente.txt', 'a')
print(fichero)


# Lectura por linea
fichero = open('fichero.txt', 'r')
linea = fichero.readline()
print(linea)
linea = fichero.readline() # En esta lee la segunda linea, este es el puntero
print(linea)
linea = fichero.readline()
print(linea)
linea = fichero.readline() # Vacio..
print(linea)
fichero.close()

# De esta manera recorremos con un for el fichero..
print("\nWITH OPEN")
with open('fichero.txt','r') as fichero:
    for linea in fichero:
        print(linea)