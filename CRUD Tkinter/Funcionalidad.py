from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3

def salir_aplicacion(raiz):

    valor_salir=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")

    if valor_salir== "yes":
        raiz.destroy()


def limpiar_entry(campo1, campo2, campo3, campo4, campo5):
    campo1.set("")
    campo2.set("")
    campo3.set("")
    campo4.set("")
    campo5.set("")
    #texto_comentario.delete(1.0, END)