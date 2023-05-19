import csv
import os
from csv import DictWriter
""" 3. El archivo cotizaciones.csv contiene las cotizaciones de las empresas de la Bolsa de valores de Colombia 
con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de pesos).

Construir una función reciba el archivo de cotizaciones y devuelva un diccionario con los datos 
del archivo por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior y cree un archivo 
en formato csv con el valor promedio de cada columna. """
def agregar():
    encabezado = ["Nombre","Final","Maximo","Minimo","Volumen","Efectivo"]
    os.system("clear")
    data ={"Nombre": input("ingrese el nombre de la empresa\n"), 
                            "Final": input("ingrese el precio de la acción al cierre de bolsa\n"),
                            "Maximo": input("ingrese el precio máximo de la acción durante la jornada\n"),
                            "Minimo": input("ingrese el precio mínimo de la acción durante la jornada\n"),
                            "Volumen": input("ingrese el volumen al cierre de bolsa\n"),
                            "Efectivo": input("ingrese la capitalización al cierre en miles de pesos\n")}
    with open("cotizaciones.csv","a",newline="") as archivo:
        archivoCSV = DictWriter(archivo, fieldnames=encabezado)
        archivoCSV.writerow(data)
        archivo.close()
def consultar():
    datos = ""
    with open("cotizaciones.csv") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        for i in lector:
            for j in i:
                valor= j.ljust(15-len(j))
                datos+=(valor)+"\t"
            print(datos)
            datos = ""
consultar()