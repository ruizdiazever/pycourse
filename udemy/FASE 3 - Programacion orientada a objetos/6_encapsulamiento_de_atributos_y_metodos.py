# EJEMPLO 1: atributos y metodos privados van con __
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."
    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")
e = Ejemplo()
e.__atributo_privado # AttributeError: 'Ejemplo' object has no attribute '__atributo_privado' 
e.__metodo_privado # AttributeError: 'Ejemplo' object has no attribute '__atributo_privado' 


# EJEMPLO 2: acceder al metodo privado con un metodo publico
class Ejemplo_2:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()
e_2 = Ejemplo_2()
e_2.atributo_publico()
e_2.metodo_publico()
print(e_2.atributo_publico())
