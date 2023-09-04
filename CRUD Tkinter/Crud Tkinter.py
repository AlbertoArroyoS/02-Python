from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

#Creo conexion con la BBDD

def conectar_BBDD():
    mi_conexion=sqlite3.connect("NegocioUsuarios")

    mi_cursor= mi_conexion.cursor()

    try:
        mi_cursor.execute()

        messagebox.showinfo("BBDD","Conexion correcta a la BBDD")

    except:
        messagebox.showinfo("BBDD","No conectado a la BBDD")

#Salir de la aplicacion

def salir_aplicacion():

    valor_salir=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")

    if valor_salir== "Yes":
        root.destroy

#Opcion de borrar, asocio cada entry a una variable de control

mi_id=StringVar()
mi_nombre=StringVar()
mi_apellido=StringVar()
mi_pass=StringVar()
mi_direccion=StringVar()

#Funcion que borra los cuadros de texto

def limpiar_entry():
    mi_id.set("")
    mi_nombre.set("")
    mi_apellido.set("")
    mi_pass.set("")
    mi_direccion.set("")
    texto_comentario.delete(1.0, END)


#Creo la barra desplegable del principio del programa
barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conectar_BBDD)
bbdd_menu.add_command(label="Salir",command=salir_aplicacion)

borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar", command=limpiar_entry)

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



#Agrego un segundo parametro al entry con las variables de control

cuadro_id=Entry(mi_frame, textvariable=mi_id)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre=Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)

cuadro_apellido=Entry(mi_frame, textvariable=mi_apellido)
cuadro_apellido.grid(row=2, column=1, padx=10, pady=10)

cuadro_pass=Entry(mi_frame, textvariable=mi_pass)
cuadro_pass.grid(row=3, column=1, padx=10, pady=10)
cuadro_pass.config(show="*")

cuadro_direccion=Entry(mi_frame, textvariable=mi_direccion)
cuadro_direccion.grid(row=4, column=1, padx=10, pady=10)

texto_comentario=Text(mi_frame, width=16, height=5)
texto_comentario.grid(row=5, column=1, padx=10, pady=10)

#Barra de desplazamiento vertical
scroll_vert=Scrollbar(mi_frame, command=texto_comentario.yview)
scroll_vert.grid(row=5, column=2, sticky="nsew")
texto_comentario.config(yscrollcommand=scroll_vert.set)

#Creacion de los label

id_label=Label(mi_frame, text="Id:")
id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombre_label=Label(mi_frame, text="Nombre:")
nombre_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellido_label=Label(mi_frame, text="Apellido:")
apellido_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

contraseña_label=Label(mi_frame, text="Contaseña:")
contraseña_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccion_label=Label(mi_frame, text="Direccion:")
direccion_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarios_label=Label(mi_frame, text="Direccion:")
comentarios_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)


#Botones CRUD de acceso directo abajo

mi_frame_botones=Frame(root)
mi_frame_botones.pack()

boton_crear=Button(mi_frame_botones, text="Crear")
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer=Button(mi_frame_botones, text="Leer")
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar=Button(mi_frame_botones, text="Actualizar")
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(mi_frame_botones, text="Borrar")
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)







root.mainloop()

