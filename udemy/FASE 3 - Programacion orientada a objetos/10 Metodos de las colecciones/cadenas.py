# Metodo 1, para pasar una cadena a mayusculas:    .upper()
print("1.   Hola marte".upper())

# Metodo 2, para pasar una cadena a minusculas:    .lower()
print("2.   HoLa tIeRRA".lower())

# Metodo 3, convierte primer caracter mayuscula, resto en minuscula: .capitalize()
print("3.  ","ever ESTUDIANTE dE SofTwARE.".capitalize())

# Metodo 4, convierte en mayuscula la primera letra de cada palabra: .title()
print("4.   ever ruiz diaz".title())

# Metodo 5, cuenta los caracteres de un string.. discrimina mayusculas o minusculas: .count()
texto = "Hola, como estas? mi nombre es Neo.."
print("5.   El caracter 'o' aparecio",texto.count("o"),"veces en el texto.")

# Metodo 6, que marca posicion donde empieza nuestra busqueda: .find()
texto_2 = "Majid Jordan"
print("6.   La palabra empieza en la posicion:",texto_2.find("Jordan"))

# Metodo 7, marca la posicion de la ultima cadena que buscamos, revers find: rfind()
texto_3 = "Majid Jordan Jordan"
print("7.   La ultima palabra empieza en la posicon:",texto_3.rfind("Jordan"))

# Metodo 8, comprueba si un string es un digito 'numero', si es correcto devuelve True: .isdigit()
c = "100"
print("8.  ",c.isdigit())

# Metodo 9, comprueba si un string tiene todos sus caracteres alfanumericos, alfabeto y numeros:
c_2 = "ABC10032po"
print("9.  ",c_2.isalnum())

# Metodo 10, comprueba si un string es solamente alfabetico, discrimina espacio:
c_3 = "HolamundoII"
print("10. ",c_3.isalpha())

# Metodo 11, comprueba si todos los caracteres de un string son minisculas..
c_4 = "Ever"
print("11. ",c_4.islower())

# Metodo 12, comprueba si todos los caracteres de un string son mayusculas..
print("12. ",c_4.isupper())

# Metodo 13, comprueba si una cadena es un titulo..
c_5 = "Bienvenidos a todes"
c_6 = "Bienvenidos Todes"
print("13. ",c_5.istitle())
print("13. ",c_6.istitle())

# Metodo 14, comprueba si un string son todos espacios..
c_7 = "     "
print("14. ",c_7.isspace())

# Metodo 15, comprueba si un string empieza con una letra o cadena, discrimina mayusculas..
c_8 = "Hola marte"
print("15. ",c_8.startswith("Hola"))

# Metodo 16, comprueba si un string termina con una letra o cadena, discrimina mayusculas..
print("16. ",c_8.endswith("marte"))

# AVANZADO
# Metodo 17, separa una cadena a partir de los espacios y crea una lista..
c_9 = "Hola marte marte"
print("17. ",c_9.split())
print("17. ",c_9.split()[0]) # De esta manera mostramos la palabra de la posicion '0'

# Metodo 18, separa una cadena a partir del caracteres elegido..
c_10 = "Hola,mundo,marte"
print("18. ",c_10.split(','))
print("18. ",c_10.split(',')[0])

# Metodo 19, separa una cadena por el caracter elegido, de esta manera..
print("19. ",".".join("EVER"))
print("19. "," ".join("EVER"))

# Metodo 20, borra espacios extras alrededor de una cadena, principio y final..
c_11 = "    Ever Toujours   "
c_12 = "---Ever Toujours---"
print("20. ",c_11.strip())
print("20. ",c_12.strip("-")) # Con esto eliminamos caracter elegido..

# Metodo 21, reemplaza caracter o palabra..
c_13 = "Hola mundo"
c_14 = "Hola mundo mundo mundo mundo"
print("21. ",c_13.replace('mundo','marte'))
print("21. ",c_13.replace('o','0'))
print("21. ",c_14.replace(" mundo","",3)) # Palabra a borrar, reemplazo, cantidad de borrados
