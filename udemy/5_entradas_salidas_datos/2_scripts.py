# Guiones con instrucciones en codigo fuente que se ejecutan
# de arriba a abajo, guardados en un fichero con un nombre
# unico y ejecutados desde el interprete.

# IMPORTANTE: pueden tomar datos (argumentos) en el momento de
# la ejecucion.

# Los argumentos siempre son tomados como cadenas, hay que
# separarlos con espacio.

# Para usar argumentos en la terminal hay que importar la
# libreria de sistema en el script <import sys>

# Los argumentos forman una lista, accedemos a ella para
# para asignar variables, etc

# EJEMPLO
import sys
nombre = (sys.argv[1]) # Asignamos a la variable nombre el PRIMER ARGUMENTO
repeticiones = int(sys.argv[2]) # Asignamos a la variable repetiones el SEGUNDO ARGUMENTO, convertismo el argumento en ENTERO, porque se toma siempre como cadena.

for i in range(repeticiones):
    print(nombre,"bienvenido. Repeticion: ",i)