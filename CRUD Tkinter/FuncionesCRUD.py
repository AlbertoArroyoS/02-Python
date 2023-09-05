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

#Funcion para crear una BBDD, consultas parametricas

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

#Funcion para leer Id que introduzcamos

def leer(Id, *args):

    global nombre_BBDD

    mi_conexion=sqlite3.connect(nombre_BBDD)

    mi_cursor=mi_conexion.cursor()

    mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + Id)

    #Almacenamos el recordset en el array

    datos_usuario=mi_cursor.fetchall()

    #recorrer cuantos args hay, y por cada campo rescato una posicion del array, desde la posicion 1 ya que la 0 corresponde al id
    posicion_array=1

    for campo in args:
        for valor_campo in datos_usuario:
            if type(campo) == Text: 
                campo.insert(1.0, valor_campo[posicion_array]) 

            else:
                campo.set(valor_campo[posicion_array])
            posicion_array +=1


    mi_conexion.commit