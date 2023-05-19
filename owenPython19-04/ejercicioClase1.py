import json
import os
""" 1. Elabore un Programa Python que lea la ruta y nombre de un archivo y muestre por pantalla la línea M del archivo.
La línea a mostrar también debe ser un dato ingresado por el usuario del programa.
Si el archivo no existe debe mostrar un mensaje por pantalla informando de ello.

2. Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de 
un cliente, 3. añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar 
guardado en el archivo de texto Directorio.txt donde el nombre del cliente y su teléfono deben aparecer separados por 
comas y cada cliente en una línea distinta.


3. El archivo cotizaciones.csv contiene las cotizaciones de las empresas de la Bolsa de valores de Colombia con las 
siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio 
máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen 
al cierre de bolsa), Efectivo (capitalización al cierre en miles de pesos).

Construir una función reciba el archivo de cotizaciones y devuelva un diccionario con los datos del archivo por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior y cree un archivo en formato csv 
con el valor promedio de cada columna. """

direccion = input("ingrese la direccion en donde esta el programa\n")
if os.path.exists(direccion) == True:
    archivo = open(direccion,"r")
    archivoTexto = archivo.readlines()
    archivo.close()
else:
    print("la direccion ingresada esta erronea")

linea = int(input("ingrese la linea del texto que desea mostrar:\n"))
for i in range(len(archivoTexto)):
    if i == linea:
        print("la linea dice:\n", archivoTexto[i-1])
        break 