# Primera forma, del modulo saludos importamos saludar
from saludos import saludar
saludar()

# Segunda forma, importamos saludos
import saludos
saludos.saludar() # hay que instanciarlo asi
s = saludos.Saludo() # creamos un objeto de "Saludo"

# Tercera forma, de saludos importamos 'Saludo'
from saludos import Saludo
Saludo() # Instanciamos


# Cuarta forma, de saludos importamos todo con '*'
from saludos import *
saludar()
Saludo()

