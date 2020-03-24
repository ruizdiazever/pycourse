import sys
sys.path.insert(1,'D:/Personal/Google Drive/dev/technologies/python/programs')
from examples import ejemplo

from io import open
from os import remove


texto = "Hola Ever\nComo estas?\nSoy Bruce Wayne"

ejemplo(1)
# Modo escritura
fichero = open('fichero_2.txt','w')
fichero.write(texto)
fichero.close()
print(fichero)


ejemplo(2)
fichero = open('fichero_2.txt','r') # Modo lectura
# Puntero apuntando al caracter 10
fichero.seek(10) # Tambien cuenta '\n'
print(fichero.read())


ejemplo(3)
print(fichero.read()) # Aca se va al final.. devuelve "vacio"


ejemplo(4)
fichero.seek(0) # Volvemos al principio
print(fichero.read())


ejemplo(5)
# Puntero en 4 '.seek(4)' hasta caracter 10 '.read(10)'
fichero.seek(5)
print(fichero.read(10))


ejemplo(6)
# Podemos saber la longitud de todo el texto y posicionarnos en el medio:
fichero.seek(0) # Puntero en inicio
texto = fichero.read()
print(fichero.seek(len(texto)/2)) # Apuntamos el puntero al medio de la cadena..
print(fichero.read(39))


ejemplo(7)
fichero.seek(0) # Puntero en primer caracter
# Situarnos al final de la primera linea
print(fichero.seek(len(fichero.readline()))) # Puntero en ultimo caracter de la primera linea
print(fichero.read()) # Mostramos lo que queda del fichero
fichero.close()

ejemplo(8)