# Funcion recursiva sin retorno
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

def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
        print("Valor final ->", num)
    return num
print(factorial(5))