lista = ["1","Ever",5,"Valentina","hannah"]

for i, elemento in enumerate(lista):
    if lista[i] == "Valentina":
        lista[i] = lista[i] + " y " + "Ever son papis de Hannah"
    else:
        pass

    if lista[i] == "hannah":
        lista[i] = elemento.upper() # De esta manera trabajamos a nivel cadena.

for i in lista:
    print(i)