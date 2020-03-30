from tkinter import *

# Configuracion de la raiz
root = Tk()
root.title("Frame")
root.resizable(1,1)
root.iconbitmap('D:/Personal/Google Drive/dev/technologies/python/udemy/FASE 4 - Temas avanzados/13 Intefaces graficas con TkInter/material/python.ico')


frame = Frame(root, width=480, height=320)  # Dimensiones..
#frame.pack()                                # Empaqueta, alinea arriba y al medio
#frame.pack(side="bottom", anchor="w") # w= oeste, e=este, s=sur, n=norte (puntos cardinales)
#frame.pack(fill='y', expand=True) # Ejes cartesianos, fill es relleno
frame.pack(fill='both', expand=True)

frame.config(cursor="pirate")               # Tipo de cursor
frame.config(bg="lightblue")                # Color de fondo, background
frame.config(bd=25)                         # Tamaño del borde en píxeles
frame.config(relief="sunken")               # Relieve del frame

root.config(cursor="arrow")               # Tipo de cursor
root.config(bg="blue")                # Color de fondo, background
root.config(bd=15)                         # Tamaño del borde en píxeles
root.config(relief="ridge")               # Relieve del frame




root.mainloop()