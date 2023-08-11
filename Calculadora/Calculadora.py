from tkinter import *

raiz = Tk()

mi_frame=Frame(raiz)

mi_frame.pack()

#Variables

operacion=""

coma=False

#Variable para ir acumulando

resultado=1

#Al pulsar se almacene en digitoDisplay y aparezca en el Entry creando una funcion 


digito_display=StringVar()

#digito_display.set("0")

display = Entry(mi_frame, textvariable=digito_display)


display.grid(row=1, column=1, columnspan=4, pady=10)

display.config(background="black", fg="green", justify="right", width=30)

#Uso funciones lambda para que no cargue automaticamente el numero 7 al cargar el programa

#------------primera fila-----------------

boton7=Button(mi_frame, text="7", width=4, command=lambda:pulsar_teclas("7"))
boton7.grid(row=2, column=1)
boton8=Button(mi_frame, text="8", width=4, command=lambda:pulsar_teclas("8"))
boton8.grid(row=2, column=2)
boton9=Button(mi_frame, text="9", width=4, command=lambda:pulsar_teclas("9"))
boton9.grid(row=2, column=3)
botondiv=Button(mi_frame, text="/", width=4)
botondiv.grid(row=2, column=4)

#------------segunda fila-----------------

boton6=Button(mi_frame, text="6", width=4, command=lambda:pulsar_teclas("6"))
boton6.grid(row=3, column=1)
boton5=Button(mi_frame, text="5", width=4, command=lambda:pulsar_teclas("5"))
boton5.grid(row=3, column=2)
boton4=Button(mi_frame, text="4", width=4, command=lambda:pulsar_teclas("4"))
boton4.grid(row=3, column=3)
botonmult=Button(mi_frame, text="*", width=4)
botonmult.grid(row=3, column=4)

#------------tercera fila-----------------

boton3=Button(mi_frame, text="3", width=4, command=lambda:pulsar_teclas("3"))
boton3.grid(row=4, column=1)
boton2=Button(mi_frame, text="2", width=4, command=lambda:pulsar_teclas("2"))
boton2.grid(row=4, column=2)
boton1=Button(mi_frame, text="1", width=4, command=lambda:pulsar_teclas("1"))
boton1.grid(row=4, column=3)
botonrest=Button(mi_frame, text="-", width=4)
botonrest.grid(row=4, column=4)

#------------cuarta fila-----------------

boton0=Button(mi_frame, text="0", width=4, command=lambda:pulsar_teclas("0"))
boton0.grid(row=5, column=1)
botoncoma=Button(mi_frame, text=".", width=4, command=lambda:pulsacion_coma())
botoncoma.grid(row=5, column=2)
botonigual=Button(mi_frame, text="=", width=4, command= lambda:total())
botonigual.grid(row=5, column=3)
botonsum=Button(mi_frame, text="+", width=4, command= lambda:suma(resultado))
botonsum.grid(row=5, column=4)

#Para que vea si hay algun numero antes pulsado, lo guarde y muestre el siguiente

def pulsar_teclas(num_pulsado):
    #Para que despues de pulsar una tecla de operacion no se acumules, solo los numeros

    global operacion
    

    if operacion != "":

        digito_display.set(num_pulsado)
        # Hay que resetear operacion de nuevo para que concatene
        operacion=""

    else:
        #que solo se pueda pulsar una vez al 0
        if num_pulsado=="0" and digito_display.get()=="0":
            digito_display.set("0")

        #Que mantenga el 0 si hemos puesto una coma para los numero decimales
        elif num_pulsado!="." and digito_display.get()=="0":
            digito_display.set(digito_display.get() + num_pulsado)

        #solucionar que no salga el cero delante 025
        elif num_pulsado!="0" and digito_display.get()=="0":
            digito_display.set(num_pulsado)
        
        else:
            digito_display.set(digito_display.get() + num_pulsado)


#--------Agregar funcionalidad a las operaciones


# funcion suma
# num va a ser lo que hay escrito en pantalla, lo que hay en el entry, lo que hay en el entry se considera texto

def suma(num):

    global operacion

    global resultado
    
    resultado+=int(num)

    operacion ="suma"

    digito_display.set(resultado)

    print(resultado)

# funcion =

def total():

    global resultado
    
    #Que haga la operacion con lo que habia antes de pulsar la operacion y lo que se pulso despues

    digito_display.set(resultado + int(digito_display.get()))

    resultado=0

# unción solo para procesar la coma y con un for recorrer la pantalla para recorrer la pantalla si encuentra una coma

def pulsacion_coma():

    contador=0

    for i in digito_display.get():

        if i==".":

            contador+=1
        
        if contador==0:

            digito_display.set(digito_display.get()+ ".")





raiz.mainloop()