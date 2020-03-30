from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()): # Aaca comprobamos si leches es True=1
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"

    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar()    # 1 si, 0 no
azucar = IntVar()   # 1 si, 0 no

imagen = PhotoImage(file='D:/Personal/Google Drive/dev/technologies/python/udemy/FASE 4 - Temas avanzados/13 Intefaces graficas con TkInter/material/giphy.gif')
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="Como quieres el cafe?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()