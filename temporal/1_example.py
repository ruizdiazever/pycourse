# EJERCICIO 1
n = int(input("Ingrese un numero entero: "))
if (n % 2) == 0:
    print(n, "es un numero par.")
else:
    print (n, "es un numero impar.")


from tkinter import *

apl = Tk()
texto = Label(apl, text="Hola Mundo!")
texto.pack()
apl.mainloop()
