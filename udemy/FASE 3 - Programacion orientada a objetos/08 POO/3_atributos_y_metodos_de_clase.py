# Atributos: Hacen referencia a las variables internas de la clase.
# Métodos: Hacen referencia a las funciones internas de la clase.

# METODO __init__
#   Es una funcion interna de la clase. Metodo es una funcion dentro de una clase.
#   Es un metodo especial para se ejecuta al crear un objeto.
#   Permite ademas enviar argumentos durante la instanciacion.
#   Parámetros en el init (argumentos al instanciar)

# PALABRA RESERVADA self
#   Hace referencia al propio objeto.
#   Sirve para diferenciar entre el ambito de clase y objeto.
#   La palabra self se utiliza dentro de las clases para diferenciar los atributos y métodos de clase del ámbito de sus métodos internos.
# SEPARADOR
def separador(num):
    print("\n=================>",num, "<=================")







# EXAMPLE 0
separador(0)
class Galleta:
    pass
una_galleta = Galleta() # Instaciamos la clase
una_galleta.sabor = "salado" # Atributo al objeto
una_galleta.color = "marron"
print("El sabor de esta galleta es",una_galleta.sabor) # Invocamos el atributo del objeto





# EXAMPLE 1
separador(1)
class Galleta_2:
    chocolate: False
g = Galleta_2()
g.chocolate = True
print(g.chocolate)





# EXAMPLE 2
separador(2)
class Galleta_3:
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta n°3")
g2 = Galleta_3()





# EXAMPLE 3
separador(3)
class Galleta_4:
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta n°4")
    def chocolatear(self): # Metodo
        self.chocolate = True # self es para acceder a la variable de clase
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :D")
        else:
            print("Soy una galleta sin chocolate :(")
g4 = Galleta_4()
g4.tiene_chocolate()
g4.chocolatear()
g4.tiene_chocolate()






# EXAMPLE 4
separador(4)
class Galleta_5:
    chocolate = False
    def __init__(self, sabor, forma): # Parametros
        self.sabor = sabor # Estas hacen referencia  la funcion, las de arriba de la clase.
        self.forma = forma
        print("Se acaba de crear una galleta {} y {}.".format(sabor,forma))
    def chocolatear(self): # Metodo
        self.chocolate = True # self es para acceder a la variable de clase
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :D")
        else:
            print("Soy una galleta sin chocolate :(")
g5 = Galleta_5("salada","redonda")




# EXAMPLE 5: agregamos un valor por defecto en los parametros.
separador(5)
class Galleta_6:
    chocolate = False
    def __init__(self, sabor=None, forma=None): # Parametros
        self.sabor = sabor # Estas hacen referencia  la funcion, las de arriba de la clase.
        self.forma = forma
        if sabor is not None and forma is not None:
            print("Se acaba de crear una galleta {} y {}.".format(sabor,forma))
        else:
            print("Esta galleta no tiene sabor ni forma.")
    def chocolatear(self): # Metodo
        self.chocolate = True # self es para acceder a la variable de clase
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :D")
        else:
            print("Soy una galleta sin chocolate :(")
g6 = Galleta_6()
g6 = Galleta_6("exquisita","grande")