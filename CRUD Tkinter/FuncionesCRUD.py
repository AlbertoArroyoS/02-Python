from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3

#Variable para que se guarde el nombre de la BBDD a la que hago conexion

nombre_BBDD=""

#funcion para almacenar el nombre de la funcion en la variable
#Crear la variable global para utilizarlo en las funciones CRUD

def almacena(nom_BD):
    global nombre_BBDD
    nombre_BBDD=nom_BD

def crear(*args):
    mi_conexion=sqlite3.connect(nombre_BBDD)

    mi_cursor=mi_conexion.cursor()

    #opcion vieja
    '''mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + mi_nombre.get() +
                        "','" + mi_apellido.get() + 
                        "','" + mi_pass.get() +
                        "','" + mi_direccion() + 
                        "','" + texto_comentario.get("1.0", END)+ "')'")'''

    #los_datos=mi_nombre.get(), mi_apellido.get(), mi_pass.get(), mi_direccion.get(), texto_comentario.get("1.0", END)

    los_datos_lista=[]

    # Hay que usar .get para los stringvar de los entry y string cuando viene de un text
    for campo in args:
        
        if type(campo)==str:

            los_datos_lista.append(campo) 

        else:
            los_datos_lista.append(campo.get())

    #convertir lista a tupla para poder utilizar el execute

    los_datos=tuple(los_datos_lista)

    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(los_datos_lista))

    mi_conexion.commit()

    messagebox.showinfo("CRUD", "Registro insertado correctamente")