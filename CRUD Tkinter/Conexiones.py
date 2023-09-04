from tkinter import *
from tkinter import messagebox
import sqlite3

#Creo conexion con la BBDD

def conectar_BBDD():
    mi_conexion=sqlite3.connect("NegocioUsuarios")

    mi_cursor= mi_conexion.cursor()

    try:
        mi_cursor.execute()

        messagebox.showinfo("BBDD","Conexion correcta a la BBDD")

    except:
        messagebox.showinfo("BBDD","No conectado a la BBDD")