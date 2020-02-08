# Reglas de precedencia: 
#   1. Parentesis
#   2. Exponente
#   3. Multiplicacion
#   4. Resta
#   5. Relacionales, de izquierda a derecha
#   6. Logicos

# Ejemplo 1
a = 10
b = 5

print("1.1: ", a*b - 2**b >= 20 and not (a % b) != 0)
# 1.    a*b - 2**b >= 20 and not 0 != 0
# 2.    a*b - 10 >= 20 and not 0 != 0
# 3.    50 - 20 >= 20 and not 0 != 0
# 4.    30 >= 20 and not 0 != 0


