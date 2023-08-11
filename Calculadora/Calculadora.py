from tkinter import *

raiz = Tk()

mi_frame=Frame(raiz)

mi_frame.pack()

display = Entry(mi_frame)

display.grid(row=1, column=1, columnspan=4, pady=10)

display.config(background="black", fg="green", justify="right", width=30)




raiz.mainloop()