'''
Funciones para EDA
Fecha: 8-11-2022
Autor: Lala Yupii
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime as dt


def valoresFaltantes(df):
    '''
    Devuelve un DataFrame con los porcentajes de nulos por columna
    
    df: DataFrame a analizar
    '''
    # Tamaño total del DataFrame
    total = df.shape[0]

    # Nulos
    nulos = df.isnull().sum()

    #Ordenamos
    nulos = nulos.sort_values(ascending=False)

    #Calculamos porcentaje en relación al total del DataFrame
    nulos = nulos.apply(lambda x : x / total * 100)

    # Seteamos la cantidad de filas de salida según el DataFrame
    # para poder visualizar toda la data
    pd.set_option('display.max_rows', nulos.shape[0])

    return nulos


def porcentajeCaracter(df, col, char):
    '''
    Devuelve el porcentaje de caracteres indicados presentes dentro de
    la columna especificada

    df: DataFrame a analizar
    col: columna a evaluar
    char: caracter a buscar
    '''
    total = df.shape[0]
    caracter = df[col][df[col] == char].count()
    porcentaje = caracter * 100 / total

    return round(porcentaje, 2)


def valoresUnicos(df):
    '''
    Devuelve el porcentaje de valores únicos por columna de un DataFrame
    df: DataFrame a analizar
    '''
    # Tamaño total del DataFrame
    total = df.shape[0]

    # Únicos
    unicos = df.nunique()

    #Ordenamos
    unicos = unicos.sort_values(ascending=False)

    #Calculamos porcentaje en relación al total del DataFrame
    unicos = unicos.apply(lambda x : x / total * 100)

    # Seteamos la cantidad de filas de salida según el DataFrame
    # para poder visualizar toda la data
    pd.set_option('display.max_rows', unicos.shape[0])

    return unicos


def valoresOutliers(df, col):
    '''
    Devuelve el porcentaje de outliers por columna del DataFrame
    
    df: DataFrama a procesar
    col -> str: columna del DataFrame a analizar
    '''
    # Tamaño total del DataFrame
    total = df.shape[0]

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    BI = Q1 - 1.5 * IQR
    BS = Q3 + 1.5 * IQR

    ol = df[(df[col] < BI) | (df[col] > BS)].shape[0]

    return ol / total * 100

def graficarBar(x, y, titulo, titulo_x, titulo_y):

    '''
        Grafica un gráfico de barras
        x -> valores para el eje x
        y -> valores para el eje y
        titulo_x ->  titulo para eje x
        titulo_y ->  titulo para eje y

    '''

    plt.figure(figsize=(20,11))
    plt.title(titulo)
    plt.xlabel(titulo_x)
    plt.xticks(rotation=80)
    plt.ylabel(titulo_y)
    plots = sb.barplot(x=x, y=y, color='#4b00bb')
    #Agregamos el valor arriba de cada barrita
    for bar in plots.patches:     
        plots.annotate(format(bar.get_height(), '.2f'), 
                    (bar.get_x() + bar.get_width() / 2, 
                        bar.get_height()), ha='center', va='center', 
                    size=18, color='green', xytext=(0, 10), 
                    textcoords='offset points') 

    return plt.show()

def convertirFecha(anio, mes, dia):
    '''
    Convierte los str en objeto datetime

    anio: año de la fecha
    mes: mes de la fecha
    dia: día de la fecha
    '''
    if mes == 'January':
        mes = '1'
    if mes == 'February':
        mes = '2'
    if mes == 'March':
        mes = '3'
    if mes == 'April':
        mes = '4'
    if mes == 'May':
        mes = '5'
    if mes == 'June':
        mes = '6'
    if mes == 'July':
        mes = '7'
    if mes == 'August':
        mes = '8'
    if mes == 'September':
        mes = '9'
    if mes == 'October':
        mes = '10'
    if mes == 'November':
        mes = '11'
    if mes == 'December':
        mes = '12'

    cadena = anio + '-' + mes + '-' + dia
    fecha = dt.strptime(cadena, '%Y-%m-%d')

    return fecha
