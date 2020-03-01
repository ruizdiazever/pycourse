# Para usar las funciones fuera del programa.. hay que retonar valores?
# Para comunicarse con el exterior, las funciones pueden devolver valores al proceso principal gracias a la instrucción return.
# En el momento de devolver un valor, la ejecución de la función finalizará

# EJEMPLO 1
def test():
    return "Una cadena retornada"
    # En return se deja de ejecutar la funcion.
print("EJEMPLO 1: ",test(),"\n")

# EJEMPLO 2
c = test()
print("EJEMPLO 2: ",c,"\n")

# EJEMPLO 3
print("EJEMPLO 3: ")
def test_2():
    return [1,2,3,4,5]
print (test_2())
print (test_2()[-1],"\n") # Slicing del ultimo elemento

# EJEMPLO 4
print("EJEMPLO 4: ") 
print(test_2()[1:4])
l = test_2()
print(l[1:4],"\n")

# EJEMPLO 5
print("EJEMPLO 5: ")
def test_3():
    return "Una cadena", 20, [1,2,3]
print(test_3()) # Esto devuelve una tupla
string,num,lista = test_3()
print(num) #IMPORTANTE