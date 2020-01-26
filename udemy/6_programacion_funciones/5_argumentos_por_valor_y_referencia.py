# Los numeros se pasan por valor, las lista por referencia.


# EJEMPLO: de paso por valor
def doblar_valor(numero):
    numero*=2

n = 10
doblar_valor(n)
print(n)

# EJEMPLO 2: de paso por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores(ns)
print(ns,n)

# EJEMPLO 2: esto ayuda a prevenir que dentro de la funcion se pueda modificar la lista
def doblar_valores_copiado(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores_copiado(ns[:]) # esto hace que sea una copia
print(ns,n)

# EJEMPLO 3
def doblar_valor_2(numero):
    return numero*2
num = 10
print(doblar_valor_2(num))
print(num) # Aca num queda igual
num = doblar_valor_2(num) # Aca si cambiamos el valor de num
print(num)