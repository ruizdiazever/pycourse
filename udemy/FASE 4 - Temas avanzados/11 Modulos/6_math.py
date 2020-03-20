import math

# 1, Redondeamos el numero Pi, este es el redondeo por defecto
pi = 3.14159
print("1.   ", round(pi))
print("1.   ", round(3.4))
print("1.   ", round(3.5))
# 2, FORZAR redondeos a la baja o alta
print("\n2.   ", math.floor(3.9999)) # Redondea a la BAJA
print("2.   ", math.ceil(5.1))      # Redondea a la ALTA
# 3, VALOR ABSOLUTO
print("\n3.   ", abs(-10))
# 4, SUMAS mas estables: math.fsum
lista = [1,2,5,7]
lista_2 = [0.9999999,1,2,3]
print("\n4.   ",sum(lista))
print("4.   ",math.fsum(lista))
print("4.   ",sum(lista_2))
print("4.   ",math.fsum(lista_2))
# 5, TRUNCAMIENTO, es eliminar la parte decimal
print("\n5.   ", math.trunc(100.12345))
# 6, POTENCIA
print("\n6.   ", math.pow(2,3)) # Dos elevado a 3
# 7, RAIZ CUADRADA
print("\n7.   ", math.sqrt(9)) # Raiz cuadrada de 9
# 8, VALOR DE PI
print("8.   ", math.pi)
print("8.   ", math.e) # valor de la constante 'e' en matematicas