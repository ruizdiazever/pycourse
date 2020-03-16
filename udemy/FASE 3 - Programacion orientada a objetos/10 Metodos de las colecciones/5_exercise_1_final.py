texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"


lineas = texto.split("#") # Conversion de string en lista y separacion por '#'

for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize() # Iteramos las lineas y ponemos mayuscula a todos. Trabajamos a nivel cadena gracias a 'enumerate: linea'
    if i == 0:
        lineas[i] = lineas[i] + "..." # Se añade '...' al final de la primera linea..
    else:
        lineas[i] = "- " + lineas[i] + "." # Se añade a las demas '.' al final

# Mostramos el resultado
for i in lineas:
    print(i)
