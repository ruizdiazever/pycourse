# EJEMPLO 1
def resta(a,b):
    return a-b
print(resta(8,5))

# EJEMPLO 2: asignar valor por nombre
print(resta(b=7,a=5))

# EJEMPLO 3: asignar un valor por defecto a los parametros
def resta_2(a=None,b=None):
    if a == None or b == None:
        print("Debes enviar dos numeros a la funcion.")
        return
    else:
        return a-b
print(resta_2())