from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()


def test():
    #MessageBox.showinfo("Test","Hola mundo!") # Titulo, mensaje

    #MessageBox.showwarning("Alerta","Se necesita permisos de administrador.")

    #MessageBox.showerror("Error","Ha ocurrido un error inesperado.")

    #resultado = MessageBox.askquestion("Salir","Esta seguro de que quiere salir sin guardar?")
    #if resultado == "yes": # no
    #    root.destroy()

    #resultado = MessageBox.askokcancel("Salir", "Sobreescribir el fichero actual?")
    #if resultado: # True
    #    root.destroy()

    #resultado = MessageBox.askyesno("Salir","Esta seguro de que desea salir sin guardar cambios?")
    #if resultado:
    #    root.destroy()

    resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar.")
    if resultado:
        root.destroy()

Button(root, text="Clickeame", command=test).pack()










root.mainloop()