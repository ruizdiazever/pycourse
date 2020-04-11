# METACARACTERES
import re

def separador(cadena):
    print(f"==========================> {cadena} <==========================")

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

texto = "cuak hla hola hoola hoooooola"
patrones = ["hla", "hola", "hoola", "hoooooola"]
buscar(patrones, texto)


separador("(*)")
# NINGUNA o MAS repeticiones de la letra a su izquierda
patrones = ['ho', 'ho*', 'ho*la', 'hu*la']
buscar(patrones, texto)


separador("(+)")
# UNA o MAS repeticiones de la letra a la izquierda del meta-carácter
patrones = ['ho+']  
buscar(patrones, texto)


separador("(?)")
# UNA o NINGUNA repetición de la letra a la izquierda del meta-carácter
patrones = ['ho?', 'ho?la']  
buscar(patrones, texto)


separador("{R}")
# Con número de repeticiones explícito {n}
# Definir 'n' repeticiones exactas de la letra a la izquierda del metaacaracter
patrones = ['ho{0}la', 'ho{1}la', 'ho{2}la']
buscar(patrones, texto)


separador("{n, m}")
# Numero de repeticiones variable entre 'n' y 'm' de la letra a la izquierda.
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']
buscar(patrones, texto)