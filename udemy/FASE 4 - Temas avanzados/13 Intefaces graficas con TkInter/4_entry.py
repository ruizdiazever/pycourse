from tkinter import *
root = Tk()




# Usuario
label = Label(root, text="Usuario")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5) # "w" es oeste
entry = Entry(root)
entry.grid(row=0, column=1)
entry.config(justify="right", state="disable")
# Email
label2 = Label(root, text="Email")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry2 = Entry(root)
entry2.grid(row=1, column=1)
entry2.config(justify="center")
# Contraseña
label3 = Label(root, text="Contraseña")
label3.grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry3 = Entry(root)
entry3.grid(row=2, column=1)
entry3.config(justify="center", show="*")


root.mainloop()