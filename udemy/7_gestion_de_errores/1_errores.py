# Funcion para separar ejercicios
def mensaje(num):
    print("\nEJEMPLO",num)

# EJEMPLO 1
mensaje(1)
l = [1,2,3]
l.pop() # El metodo pop elimina el ultimo elemento
l.pop()
l.pop()
if len(l) > 1:
    print(l)
else:
    print("Lista vacia.")

# EJEMPLO 2
mensaje(2)
n = int(input("Ingrese un numero: "))
m = 4

print("{}/{}= {}".format(n,m,n/m)) # Si introducimos una cadena da error