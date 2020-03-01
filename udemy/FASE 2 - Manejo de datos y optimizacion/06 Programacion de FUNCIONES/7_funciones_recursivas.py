# Se trata de funciones que se llaman a sí mismas durante su propia ejecución. Funcionan de forma similar a las iteraciones, y 
# debemos encargarnos de planificar el momento en que una función recursiva deja de llamarse o tendremos una función rescursiva infinita.

# Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea más fácil abordar el problema y solucionarlo.


# Cuenta regresiva hasta cero a partir de un número:
# Ejemplo sencillo sin retorno
# Sirve para ejecutar & despues "eliminar" se ramifica
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooom!")
    print("Fin de la funcion", num)
cuenta_atras(5)


# Ejemplo con retorno (factorial de un número)
# El factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número:
def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
        print("Valor final ->", num)
    return num
print(factorial(5))