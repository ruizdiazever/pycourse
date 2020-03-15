# 1) Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
    # un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
    # En este otro:
#   Un día que el viento soplaba con fuerza...
        # - Mira como se mueve aquella banderola -dijo un monje.
        # - Lo que se mueve es el viento -respondió otro monje.
        # - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
#   Lo único prohibido es modificar directamente el texto

cadena = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

lista = cadena.split("#") # Separamos la cadena por '#'

# Primera frase..
cadena_0 = lista[0]
cadena_0 = "".join(cadena_0)
cadena_0 = cadena_0.capitalize()
cadena_0 = list(cadena_0)
cadena_0.append("...")
print("".join(cadena_0))
# Segunda frase..
cadena_1 = lista[1]
cadena_1 = "".join(cadena_1)
cadena_1 = cadena_1.capitalize()
cadena_1 = list(cadena_1)
cadena_1.append(".")
cadena_1.insert(0, "   - ")
print("".join(cadena_1))
# Tercera frase..
cadena_2 = lista[2]
cadena_2 = "".join(cadena_2)
cadena_2 = cadena_2.capitalize()
cadena_2 = list(cadena_2)
cadena_2.append(".")
cadena_2.insert(0, "   - ")
print("".join(cadena_2))
# Cuarta frase..
cadena_3 = lista[3]
cadena_3 = "".join(cadena_3)
cadena_3 = cadena_3.capitalize()
cadena_3 = list(cadena_3)
cadena_3.append(".")
cadena_3.insert(0, "   - ")
print("".join(cadena_3))