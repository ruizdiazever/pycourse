import sys

sys.path.insert(1,'D:/Personal/Google Drive/dev/technologies/python/udemy/FASE 4 - Temas avanzados/11 Modulos') # '..' hace referencia a un directorio anterior..
# print(sys.path) # Con esto mostramos la ruta donde Python busca el modulo..

#   Esto da error sin la especificacion de directorio, ya que Python no encuentra el modulo..
#from saludos import Saludo
#Saludo()

from saludos import saludar, Saludo
saludar()
Saludo()
