class Matematica:
    def __init__(self):
        print("Bienvenido.")
    def suma(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        print("La suma de ambos numeros es:",num_1+num_2)
    def resta(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        print("La resta de ambos numeros es:",num_1-num_2)
    def producto(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        print("El producto de ambos numeros es:",num_1*num_2)
    def division(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        print("La division de ambos numeros es:",num_1/num_2)

# Instanciamos la clase
objeto_matematico = Matematica()

while(True):
    try:
        num_1 = int(input("1. Ingrese el primer valor: "))
        num_2 = int(input("2. Ingrese el segundo valor: "))

        objeto_matematico.suma(num_1,num_2)
        objeto_matematico.resta(num_1,num_2)
        objeto_matematico.producto(num_1,num_2)
        objeto_matematico.division(num_1,num_2)
        break
    except ValueError:
        print("Error! Introduzca un numero.")
    except Exception as e:
        print(type(e).__name__)