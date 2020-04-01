from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

# La utilizaremos para almacenar la ruta del fichero
ruta = ""

# Logica
def nuevo():
    global ruta # Indicamos que la ruta es respecto a la variable global
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end") # borra del caracter 1 al final
    root.title("Mi Editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir=".",filetype=(("Fichero de texto", "*.txt"),),title="Abri un fichero de texto")
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end') # Todo menor el ultimo caracter
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi Editor")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

# Configuracion de la raiz
root = Tk()
root.title("Mi editor")

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit())
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

# Agregamos el menu al root
root.config(menu=menubar)

# Finalmente bucle de la aplicacion
root.mainloop()