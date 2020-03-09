# Herencia multiple es una caracteristica de Python que no es soportado por otros lenguajes.
    # Finalmente hablemos de la herencia múltiple: la capacidad de una subclase de heredar de múltiples superclases.
    # Esto conlleva un problema, y es que si varias superclases tienen los mismos atributos o métodos, la subclase sólo podrá heredar de una de ellas.
    # En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase:


class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este metodo lo heredo de A")


class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este metodo lo heredo de B")
        

print("EJEMPLO 1: ")
class C(A,B): # Prioridad a la clase izquierda..
    def c(self):
        print("Este metodo es de C2")


class D(B,A):
    pass
    # Ejemplos:
c = C() # Aca hereda de la 'class A'
d = D() # Aca hereda de la 'class B


print("\nEJEMPLO 2: ")
c2 = C()
c2.a() # Metodo de 'Class A'
c2.b() # Metodo de 'Class B'
c2.c() # Metodo propio de 'Class C2'
