from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
from FuncionesCRUD import *

#Creo conexion con la BBDD

def conectar_BBDD():

    nombre_BBDD = simpledialog.askstring("BBDD", "Indroduzca el nombre de la BBDD")

    #Llamar a la funcion almacena de FuncionesCrud para guardar ese nombre en la variable global
    almacena(nombre_BBDD)
    mi_conexion = sqlite3.connect(nombre_BBDD)

    mi_cursor = mi_conexion.cursor()

    try:
        mi_cursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(80),
                PASSWORD VARCHAR(50),
                DIRECCION VARCHAR(80),
                COMENTARIOS VARCHAR(200)
            )
        ''')

        mi_conexion.commit()

        messagebox.showinfo("BBDD", "BBDD Creada correctamente")

    except sqlite3.OperationalError:
        
        messagebox.showinfo("BBDD", "La BBDD ya existe")