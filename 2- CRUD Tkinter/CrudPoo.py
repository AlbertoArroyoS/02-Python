#2-CRUD orientado a objetos, adaptado del basico inicial Crud Tkinter.py 

from tkinter import *
from tkinter import messagebox
import sqlite3
from Conexiones import *
from Funcionalidad import *
from FuncionesCRUD import *

class CrudPOO(Frame):

    #constructor

    def __init__(self, raiz):

        raiz.title("Gestor BBDD Alberto")

        #Variables de control que guardan los datos de cada entry

        self.mi_id=StringVar()
        self.mi_nombre=StringVar()
        self.mi_apellido=StringVar()
        self.mi_pass=StringVar()
        self.mi_direccion=StringVar()

        #Barra de menu

        self.barra_menu=Menu(root)
        raiz.config(menu=self.barra_menu)



        super().__init__(raiz, width=300, height=300)
        self.master=raiz
        self.pack()

        self.mi_frame_botones=Frame(raiz)
        self.mi_frame_botones.pack()

        self.crear_widgets()

        self.crear_barra_menu()

        self.ubicar_botones()


    def crear_widgets(self):

        self.cuadro_id=Entry(self, textvariable=self.mi_id)
        self.cuadro_id.grid(row=0, column=1, padx=10, pady=10)

        self.cuadro_nombre=Entry(self, textvariable=self.mi_nombre)
        self.cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.cuadro_apellido=Entry(self, textvariable=self.mi_apellido)
        self.cuadro_apellido.grid(row=2, column=1, padx=10, pady=10)

        self.cuadro_pass=Entry(self, textvariable=self.mi_pass)
        self.cuadro_pass.grid(row=3, column=1, padx=10, pady=10)
        self.cuadro_pass.config(show="*")

        self.cuadro_direccion=Entry(self, textvariable=self.mi_direccion)
        self.cuadro_direccion.grid(row=4, column=1, padx=10, pady=10)

        self.texto_comentario=Text(self, width=16, height=5)
        self.texto_comentario.grid(row=5, column=1, padx=10, pady=10)

        #Barra de desplazamiento vertical
        self.scroll_vert=Scrollbar(self, command=self.texto_comentario.yview)
        self.scroll_vert.grid(row=5, column=2, sticky="nsew")
        self.texto_comentario.config(yscrollcommand=self.scroll_vert.set)

        #Creacion de los label

        self.id_label=Label(self, text="Id:")
        self.id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.nombre_label=Label(self, text="Nombre:")
        self.nombre_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.apellido_label=Label(self, text="Apellido:")
        self.apellido_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        self.contraseña_label=Label(self, text="Contaseña:")
        self.contraseña_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        self.direccion_label=Label(self, text="Direccion:")
        self.direccion_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        self.comentarios_label=Label(self, text="Comentarios:")
        self.comentarios_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

    def crear_barra_menu(self):

        #Creo la barra desplegable del principio del programa

        self.bbdd_menu=Menu(self.barra_menu, tearoff=0)
        self.bbdd_menu.add_command(label="Conectar", command=conectar_BBDD)
        self.bbdd_menu.add_command(label="Salir", command=lambda:salir_aplicacion(root))

        self.borrar_menu=Menu(self.barra_menu, tearoff=0)
        self.borrar_menu.add_command(label="Limpiar campos", command=lambda:limpiar_entry(self.texto_comentario, self.mi_id, self.mi_nombre,
        self.mi_apellido,self.mi_pass,self.mi_direccion))

        self.crud_menu=Menu(self.barra_menu, tearoff=0)
        self.crud_menu.add_command(label="Crear", command=lambda:crear(self.mi_nombre, self.mi_apellido, self.mi_pass, self.mi_direccion,self.texto_comentario.get(1.0, END)))
        self.crud_menu.add_command(label="Leer", command=lambda:leer(self.mi_id.get(), self.mi_nombre, self.mi_apellido, self.mi_pass, self.mi_direccion,self.texto_comentario))
        self.crud_menu.add_command(label="Actualizar", command=lambda:actualizar(self.mi_id.get(),self.mi_nombre, self.mi_apellido, self.mi_pass, self.mi_direccion,self.texto_comentario.get(1.0, END)))
        self.crud_menu.add_command(label="Borrar", command= lambda:eliminar(self.mi_id.get()))

        self.ayuda_menu=Menu(self.barra_menu, tearoff=0)
        self.ayuda_menu.add_command(label="Licencia", command=lambda:messagebox.showinfo("Licencia", "BBDD Tkinter"))
        self.ayuda_menu.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de", "Prueba Aplicacion CRUD Alberto Arroyo"))

        self.barra_menu.add_cascade(label="BBDD", menu=self.bbdd_menu)
        self.barra_menu.add_cascade(label="Borrar", menu=self.borrar_menu)
        self.barra_menu.add_cascade(label="CRUD", menu=self.crud_menu)
        self.barra_menu.add_cascade(label="Ayuda", menu=self.ayuda_menu)

    def ubicar_botones(self):

        self.boton_crear=Button(self.mi_frame_botones, text="Crear", command=lambda:crear(self.mi_nombre, self.mi_apellido, self.mi_pass, self.mi_direccion,self.texto_comentario.get(1.0, END)))
        self.boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.boton_leer=Button(self.mi_frame_botones, text="Leer", command=lambda:leer(self.mi_id.get(), self.mi_nombre, self.mi_apellido, self.mi_pass, self.mi_direccion,self.texto_comentario))
        self.boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.boton_actualizar=Button(self.mi_frame_botones, text="Actualizar", command=lambda:actualizar(self.mi_id.get(),self.mi_nombre, self.mi_apellido, self.mi_pass, self.mi_direccion,self.texto_comentario.get(1.0, END)))
        self.boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

        self.boton_borrar=Button(self.mi_frame_botones, text="Borrar", command= lambda:eliminar(self.mi_id.get()))
        self.boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

        self.boton_borrar=Button(self.mi_frame_botones, text="Limpiar campos", command=lambda:limpiar_entry(self.texto_comentario, self.mi_id, self.mi_nombre,
        self.mi_apellido,self.mi_pass,self.mi_direccion))
        self.boton_borrar.grid(row=1, column=4, sticky="e", padx=10, pady=10)



root=Tk()
app=CrudPOO(root)
app.mainloop()