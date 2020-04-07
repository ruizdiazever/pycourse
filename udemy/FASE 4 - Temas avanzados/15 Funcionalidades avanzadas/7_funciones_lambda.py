# https://docs.hektorprofe.net/python/funcionalidades-avanzadas/funciones-lambda/

# EJEMPLO 1
def doblar(num):
    resultado = num * 2
    return resultado

print(doblar(5))

# EJEMPLO 2
def doblar(num):
    return num * 2

# EJEMPLO 3
def doblar(num): return num * 2

# LAMBDA
doblar = lambda num: num * 2
print(doblar(2))

# LAMBDA 2
impar = lambda num: num % 2 != 0
print(impar(9))

# LAMBDA 3
revertir = lambda cadena: cadena[::-1]
print(revertir("HANNAH"))
print(revertir("EVER"))

# LAMBDA 4
sumar = lambda x,y: x+y
print(sumar(5,8))