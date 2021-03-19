import sys

if len(sys.argv) == 3:
    """Al ejecutar el script le indicamos el string y un integer para la cantidad de repeticiones """
    nombre = (sys.argv[1])
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(nombre, "bienvenido", i)
else:
    print("ERROR, introduce los argumentos correctamente.")
    print('EJEMPLO: python 5_test.py "Texto" 5')