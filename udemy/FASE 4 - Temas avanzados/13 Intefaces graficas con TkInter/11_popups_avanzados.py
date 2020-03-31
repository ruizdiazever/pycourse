from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test_color():
    color = ColorChooser.askcolor(title="Elige un color")
    print(color)

def test_ruta():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero")
    print(ruta)

def test_ruta_2():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:")
    print(ruta)

def test_ruta_3():
    ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:",
    filetypes=  (
                ("Fichero de texto","*.txt"),
                ("Fichero de texto avanzado","*.txt2"),
                ("Todos los ficheros","*.*")
                ))
    print(ruta)

def guardar(): # Equivale a open('ruta'.'w')
    #fichero = FileDialog.asksaveasfile(title="Guardar un fichero.")
    #fichero = FileDialog.asksaveasfile(title="Guardar un fichero.", mode="r+", defaultextension=".txt")
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero.", mode="w", defaultextension=".txt")

    if fichero is not None:
        fichero.write("Hola marte")
        fichero.close()


Button(root, text="Click", command=guardar).pack()

root.mainloop()