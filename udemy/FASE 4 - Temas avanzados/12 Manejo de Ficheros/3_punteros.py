import sys
sys.path.insert(1,'D:/Personal/Google Drive/dev/technologies/python/programs')
from examples import ejemplo

from io import open
from os import remove


texto = "Hola Ever\nComo estas?\nSoy Bruce Wayne"

ejemplo(1) # EJEMPLO BASICO
fichero = open('fichero.txt','w') # Modo escritura
fichero.write(texto)
fichero.close()
print(fichero)


ejemplo(2) # PUNTERO EN CIERTA POSICION
fichero = open('fichero.txt','r') # Modo lectura
# Puntero apuntando al caracter 10
fichero.seek(10) # Tambien cuenta '\n'
print(fichero.read())


ejemplo(3) # PUNTERO EN FINAL
print(fichero.read()) # Aca se va al final.. devuelve "vacio"


ejemplo(4) # PUNTERO AL PRINCIPIO
fichero.seek(0) # Volvemos al principio
print(fichero.read())


ejemplo(5) # PUNTERO EN CIERTA POSICION HASTA CIERTA POSICION
# Puntero en 4 '.seek(4)' hasta caracter 10 '.read(10)'
fichero.seek(5)
print(fichero.read(10))


ejemplo(6) # PUNTERO AL MEDIO DEL STRING
# Podemos saber la longitud de todo el texto y posicionarnos en el medio:
fichero.seek(0) # Puntero en inicio
texto = fichero.read()
print(fichero.seek(len(texto)/2)) # Apuntamos el puntero al medio de la cadena..
print(fichero.read(39))


ejemplo(7) # PUNTERO AL FINAL DE LINEA
fichero.seek(0) # Puntero en primer caracter
# Situarnos al final de la primera linea
print(fichero.seek(len(fichero.readline()))) # Puntero en ultimo caracter de la primera linea
print(fichero.read()) # Mostramos lo que queda del fichero
fichero.close()


ejemplo(8) # LECTURA MAS ESCRITURA:
fichero = open('fichero.txt', 'r+') # Lectura + escritura..
fichero.seek(0)
fichero.write('ASDFGHJKL')
fichero.seek(0)
print(fichero.read())
fichero.close()


ejemplo(9) # CONTENIDO EN 3RA LINEA
fichero = open('fichero.txt','r+')
fichero.seek(0)
lineas = fichero.readlines()
lineas[2] = "Esta linea  la he modificado en memoria"
print(lineas)
lineas = fichero.writelines(lineas) # Aca guardamos en memoria..
fichero.close()