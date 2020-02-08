# EJEMPLO 1
def saludar():
    print("Hola, este print se llama desde la funcion 'saludar()'")
saludar() # Se ejecuta simplemente de esta forma

# EJEMPLO 2
def dibujar_tabla_del_5():
    for i in range(1,11):
        print("{} x {}= {}".format(5,i,5*i))
dibujar_tabla_del_5()

# EJEMPLO 3
def test():
    n = 10
test()

# EJEMPLO 4
m = 10
def test_2():
    print(m)
test_2() # Se nos muestra el valor de m a pesar de que no esta dentro de la funcion

# EJEMPLO 5
def test_3():
    print(l)
l = 10 # Un requisito para ejecutar la funcion es que la variable este antes de la ejecucion..
test_3()

# EJEMPLO 6
# Al crear una variable del mismo nombre dentro de la funcion y otra afuera coexisten independientemente.
# Hay que tratar de evitar esto.
def test_4():
    o = 5
    print(o)
test_4()
o = 10
test()
print(o)