""" Preparación y limpieza
Lo último importante a comentar es que la clase TestCase incorpora 
dos métodos extras.

El primero es 
setUp() <--------------------------------
y sirve para preparar el contexto de las pruebas, 
por ejemplo para escribir unos valores de prueba en un fichero conectarse 
a un servidor o a una base de datos.

Luego tendríamos 
tearDown() <--------------------------------
para hacer lo propio con la limpieza, 
borrar el fichero, desconectarse del servidor o borrar las entradas 
de prueba de la base de datos.

Este proceso de preparar el contexto se conoce como test fixture 
o accesorios de prueba.

Sólo por poner un ejemplo supongamos que necesitamos contar con una 
lista de elementos para realizar una serie de pruebas: """


import unittest

def doblar(a): return a*2

class PruebaTestFixture(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)


if __name__ == '__main__':
    unittest.main() 