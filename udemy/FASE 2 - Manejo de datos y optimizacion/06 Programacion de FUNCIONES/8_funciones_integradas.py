# Muchas veces es para conversiones entre tipos de datos
# Otras para manipular informacion

n = int("10")
f = float("10.5")
c = str("Un texto y un numero " + str(10) + " " + str(3.14))

print(n)
print(f)
print(c)
print(bin(10)) # Convertimos 10 a binario
print(hex(10)) # Exadecimal de 10

# BINARIO Y HEXADECIMAL
print(int('0b1010',2)) # Binario en base 2
print(int('0xa',16)) # Hexadecimal en base 16

# VALOR ABSOLUTO DE NUMERO
print(abs(55))
print(abs(-70))

# REDONDEAR, redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza
print(round(5.5))

# EVALUAR UNA EXPRESION EN CADENA
print(eval('2+5'))
num = 15
print(eval('num*10 - 5'))

# LONGITUD
print(len("Hola programador"))
print(len([]))

# HELP! Invocar el menú de ayuda del intérprete de Python
print(help())