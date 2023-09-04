from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3

def salir_aplicacion(raiz):

    valor_salir=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")

    if valor_salir== "yes":
        raiz.destroy()


def limpiar_entry(cuadro_texto, *args):
    for campo in args:
        campo.set("")

    cuadro_texto.delete(1.0, END)
