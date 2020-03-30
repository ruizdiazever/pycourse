from tkinter import *

root = Tk()

""" # Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="Hola Hannah").pack(anchor="nw") # noroeste
label = Label(root, text="Hola Ever")
label.pack(anchor="center")
Label(root, text="Hola Valen").pack(anchor="se") # sureste

label.config(bg="green", fg="white", font=("Verdana",24))
label.config(textvariable=texto) """

imagen = PhotoImage(file='D:/Personal/Google Drive/dev/technologies/python/udemy/FASE 4 - Temas avanzados/13 Intefaces graficas con TkInter/material/giphy.gif')
Label(root, image=imagen, bd=0).pack(side="left")

root.mainloop()