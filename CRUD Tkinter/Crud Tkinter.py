from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()


#Creo la barra desplegable del principio del programa
barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar")
bbdd_menu.add_command(label="Salir")

borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar")

crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

#Construyo los campos Grid a rellenar, con el id, nombre, password, apellido y direccion

mi_frame=Frame(root)
mi_frame.pack()


cuadro_id=Entry(mi_frame)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre=Entry(mi_frame)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)

cuadro_pass=Entry(mi_frame)
cuadro_pass.grid(row=2, column=1, padx=10, pady=10)
cuadro_pass.config(show="*")

cuadro_direccion=Entry(mi_frame)
cuadro_direccion.grid(row=3, column=1, padx=10, pady=10)




root.mainloop()

