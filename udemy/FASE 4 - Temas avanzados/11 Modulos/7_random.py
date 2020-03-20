import random

# 1, GENERAR NUMERO ALEATORIO
print("1.   ", random.random()) # valor >= 0 and < 1.0

# 2, GENERAR CON RANGO
print("2.   ", random.uniform(1,10))

# 3, GENERAR ENTERO CON RANGO
print("3.   ", random.randrange(10)) # Del 0 a menor a 10
print("3.   ", random.randrange(-50,150))

# 4, GENERAR CARACTER ALEATORIO DE UNA CADENA
cadena = "Hola marte"
print("4.   ", random.choice(cadena))

# 5, CHOICE con lista
lista = [1,"Hola","-99","marte","mundo"]
print("5.   ", random.choice(lista))

# 6, DESORDENAR una lista aleatoriamente
random.shuffle(lista)
print("6.   ", lista)

# 7, TOMAR una muestra aleatoria de una lista o coleccion..
print("7.   ", random.sample(lista, 3)) # lista y cantidad de muestras
