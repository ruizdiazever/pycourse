a = 0
a += 1 # Suma en asignacion, incrementa.
print(a)


b= 50
b -= 10 # Resta en asignacion, disminuye.
print(b)


c = 5
c *= 2 # Producto en asignacion, multiplica.
print(c)


d = 100
d /= 2 # Division en asignacion, divide.
print(d)


e = 200
e %= 7 # Modulo en asignacion, resto.
print(e)

f = 2
f **= 3 # Potencia en asignacion, potencia.
print(f)

# RESUMEN DE LA UNIDAD
n = 0 # Asignacion de 0 en n
while n < 10: # Expresion relacional n < 10, devuelve True, porque n empieza en 0
    if (n % 2) == 0: # Expresion aritmetica y expresion relacional
        print(n, "Es un numero par")
    else:
        print(n, "Es un numero impar")
    n += 1 # Expresion aritmetica n = n + 1 equivalente a operacion en asignacion n+=1