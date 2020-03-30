# 1, importamos tkinter!
from tkinter import *

# 2, creamos la  raiz..
root = Tk()

# 3, titulo de la ventana
root.title("GLaDOS")

# 4, Desactivar redimensión de ventana (Ancho, Altura)
root.resizable(0,0) # Argumentos (False, False)
root.resizable(1,1) # Argumentos (True, True)

# 5, Añadir icono a la ventana
root.iconbitmap('D:/Personal/Google Drive/dev/technologies/python/udemy/FASE 4 - Temas avanzados/13 Intefaces graficas con TkInter/material/python.ico')

# 6, si cambiamos la extension de nuestro archivo 'tk.py' a 'tk.pyw' se ejecuta
#   el programa sin la terminal






# 3, Comenzamos el bucle de aplicación, es como un while True
# IMPORTANTE: siempre debajo de todo.
root.mainloop()