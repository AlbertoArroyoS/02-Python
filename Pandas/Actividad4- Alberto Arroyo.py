# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# ACTIVIDAD 4- ALBERTO ARROYO SANTOFIMIA
# REALIZADA EN SPYDER

# libreria de pandas
import pandas as pd
# libreria numpy
import numpy as np
# libreria de dibujo matematico
import matplotlib.pyplot as plt

import matplotlib
# libreria para plotear
matplotlib.style.use('ggplot')

# Colores para cada columna
colors = ["#FF0000", "#00FF00", "#FFFF00"]

data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Month': ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9]
}
# Creo el dataframe           
df = pd.DataFrame(data)
# Establecemos cual es el indice, el eje x, y y los valores
pivot_df = df.pivot(index='Year', columns='Month', values='Value')

#Cambio estilo
plt.style.use(["dark_background"]) 

# Cambiar los colores para cada columna y aumentar el ancho
pivot_df.loc[:, ['Jan', 'Feb', 'Mar']].plot.bar(stacked=True, color=colors, figsize=(10, 7), width=0.8)

#Titulo del gráfico con mi nombre y en negrita
plt.title("Actividad 4 Alberto Arroyo",fontweight= "bold")

#Cuadricula en gris          
plt.grid(True, linestyle="-.",c="gray")

#lo mostramos
plt.show()


##Pruebas de Alberto de Pandas, resultados por consola

#Analizar los datos de un dataframe por consola
print("Analizar los datos de un dataframe por consola")
print(df.info())
print("----------------------------------------")

# analizar datos de tipo numérico
#print(df.describe())

#Analizar datos de tipo numérico de una columna, value en este caso
print("Analizar datos de tipo numérico de una columna, value en este caso")
print(df.Value.describe())
print("----------------------------------------")

#Análisis solo de las columnas de tipo numerico , importar numpy, dice el tipo de dato que tiene
print("Análisis solo de las columnas de tipo numerico con numpy")
print(df.Value.describe(include=[np.number])) 
print("----------------------------------------")
#Análisis solo de las columnas de tipo texto
#print(df.Value.describe(include=[object])) 

#Ver la info del dataframe de los primeros registros
print("Ver la info del dataframe de los primeros registros")
print(df.head())
print("----------------------------------------")      

#Muestra los últimos registros del dataframe
print("Muestra los últimos registros del dataframe")
print(df.tail())
print("----------------------------------------")  

#Propiedad que nos va a mostrar cuantas filas y columnas tiene un dataframe
print("Mostrar cuantas filas y columnas tiene un dataframe")
print(df.shape)
print("----------------------------------------")  

#Propiedad para ver cuáles son las columnas que tenemos en el dataframe
print("Cuáles son las columnas que tenemos en el dataframe")
print(df.columns)
print("----------------------------------------") 

#Para ver la información de una sola columna
print("Para ver la información de una sola columna")
print(df["Month"])
#print(df.Month)  Otra forma, mismo resultado
print("----------------------------------------") 

#Ver la informacion en formato lista
print("Ver la informacion en formato lista")
print(list(df.Month))
#print(df.Month)  Otra forma, mismo resultado
print("----------------------------------------") 

#Reemplazar una columna por otra 
#df.Value = df["Month"]

#Eliminar una columna de un dataframe
#df.drop([Month], axis=1, inplace=True)

#Eliminar filtrando por listas
#dataframe=dataframe[listaCreada]

#Renombrar columnas
df.rename(columns={"Value":"Valor"}, inplace=True)
df.rename(columns={"Month":"Mes"}, inplace=True)
df.rename(columns={"Year":"Año"}, inplace=True)
print(df.columns)
print("----------------------------------------") 

# Funciones y medidas para realizar cálculos con los datos de un dataframe

#Crear una nueva, donde segun los valores de valor ponga una frase
df["TablaNueva"]= df["Valor"].map({1:"Cuesta de enero", 5:"Vacaciones", 7:"Vuelta a clase"})
print(df)
print("----------------------------------------") 

#Funcion para poner contenido de una tabla en mayusculas
def en_mayusculas(x):
    return x.upper()

#Poner los nombres a mayúsculas con una función
#applymap es útil si queremos transformar todos los valores del dataframe o varias columnas
df[["Mes"]] = df[["Mes"]].applymap(en_mayusculas)
print(df)
print("----------------------------------------") 


