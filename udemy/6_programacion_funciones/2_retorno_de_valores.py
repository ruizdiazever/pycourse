# Para usar las funciones fuera del programa..

# EJEMPLO 1
def test():
    return "Una cadena retornada"
    # En return se deja de ejecutar la funcion.
print(test())

# EJEMPLO 2
c = test()
print(c)

# EJEMPLO 3
def test_2():
    return [1,2,3,4,5]
print (test_2())
print (test_2()[-1]) # Slicing del ultimo elemento

# EJEMPLO 4
print(test_2()[1:4])
l = test_2()
print(l[1:4])

# EJEMPLO 5
def test_3():
    return "Una cadena", 20, [1,2,3]
print(test_3()) # Esto devuelve una tupla
string,num,lista = test_3()
print(num) #IMPORTANTE