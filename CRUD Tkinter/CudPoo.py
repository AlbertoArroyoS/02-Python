#2-CRUD basado en el original Crud Tkinter.py orientado a objetos

from tkinter import *
from tkinter import messagebox
import sqlite3

class CrudPOO(Frame):

    #constructor

    def __init__(self, raiz):


        #Variables de control que guardan los datos de cada entry

        self.mi_id=StringVar()
        self.mi_nombre=StringVar()
        self.mi_apellido=StringVar()
        self.mi_pass=StringVar()
        self.mi_direccion=StringVar()


        super().__init__(raiz, width=300, height=300)
        self.master=raiz
        self.pack

        self.crear_widgets()

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

        self.comentarios_label=Label(self, text="Direccion:")
        self.comentarios_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

    def crear_barra_menu(self):

        #Creo la barra desplegable del principio del programa

        bbdd_menu=Menu(self.barra_menu, tearoff=0)
        bbdd_menu.add_command(label="Conectar", command=conectar_BBDD)
        bbdd_menu.add_command(label="Salir",command=salir_aplicacion)

        borrar_menu=Menu(self.barra_menu, tearoff=0)
        borrar_menu.add_command(label="Limpiar campos", command=limpiar_entry)

        crud_menu=Menu(self.barra_menu, tearoff=0)
        crud_menu.add_command(label="Crear", command=crear)
        crud_menu.add_command(label="Leer", command=leer)
        crud_menu.add_command(label="Actualizar", command=actualizar)
        crud_menu.add_command(label="Borrar", command=eliminar)

        ayuda_menu=Menu(self.barra_menu, tearoff=0)
        ayuda_menu.add_command(label="Licencia")
        ayuda_menu.add_command(label="Acerca de")

        self.barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
        self.barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
        self.barra_menu.add_cascade(label="CRUD", menu=crud_menu)
        self.barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)





root=Tk()
app=CrudPOO(root)
app.mainloop()