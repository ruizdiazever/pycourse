# 1) Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales.
"Hola Mundo"      # String
[1, 10, 100]      # List
-25               # Int          
1.167             # Float   
["Hola", "Mundo"] # Lista
' '               # String



# 2) Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a 
# partir de las siguientes variables:
a = 10
b = -5
c = "Hola "
d = [1, 2, 3]
print(a * 5)        # 50
print(a - b)        # 15
print(c + "Mundo")  # Hola Mundo
print(c * 2)        # Hola Hola
print(c[-1])        # Devuelve un espacio
print(c[1:])        # ola
print(d + d)        # [1, 2, 3] [1, 2, 3]



# 3) El siguiente código pretende realizar una media entre 3 números, pero no funciona 
# correctamente. ¿Eres capaz de identificar el problema y solucionarlo?
numero_1 = 9
numero_2 = 3
numero_3 = 6

# media = numero_1 + numero_2 + numero_3 / 3
media = (numero_1 + numero_2 + numero_3) / 3 # Es respetar las reglas de precedencia..
print("La nota media es", media)



# 4) Vamos a suponer que cada número es una nota, y lo que 
# queremos es obtener la nota media. El problema es que cada nota tiene un valor porcentual:
#       La primera nota vale un 15% del total
#       La segunda nota vale un 35% del total
#       La tercera nota vale un 50% del total
# Desarrolla un programa para calcular perfectamente la nota final.
nota_1 = 10
nota_2 = 7
nota_3 = 4
media = nota_1*0.15 + nota_2*0.35 + nota_3*0.50
print ("La nota media del ejercicio 4 es: ", media)



# 5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que 
# en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. 
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

# Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista 
# ¡Pruébalo!

matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

matriz[1][-1] = 6
matriz[-1][-1] = sum(matriz[3][:-1]) # Otra forma de resolverlo

print("La suma de la primera lista es: ",sum(matriz[0]))
print("La suma de la segunda lista es: ",sum(matriz[1]))
print("La suma de la tercera lista es: ",sum(matriz[2]))
print("La suma de la cuarta lista es: ",sum(matriz[3]))

# 6) Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al 
# revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos 
# formatear la cadena y conseguir una estructura como la siguiente?:

# Nombre Apellido ha sacado un Nota de nota.
# Ayuda: Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"

cadena = cadena[::-1] # Invertimos cadena IMPORTANTE TRUCO
print(cadena) # Vemos cadena invertida
print(cadena[3:],"ha sacado un",cadena[0:2],"de nota.") # Finalizamos ejercicio.