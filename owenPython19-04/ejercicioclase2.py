import os
import time
if not os.path.exists("Directorio.txt"):
    directorio = open("Directorio.txt","w")
else:
    directorio = open("Directorio.txt","r")

def menu():
    os.system("clear")
    print("BIENVENIDO")
    print("que desea hacer?:\n1. añadir el teléfono de un nuevo cliente\n2. para consultar el teléfono de un cliente\n3. eliminar el teléfono de un cliente\n0. salir")
def agregarCliente():
    os.system("clear")
    print("AGREGAR")
    nombre = input("ingrese el nombre del cliente")
    telefono = input("ingrese el numero del teléfono")
    cliente = str(nombre)+","+str(telefono)+"\n"
    with open("Directorio.txt","a") as archivo:
        archivo.write(cliente)
        directorio.close()
    print("cliente añadido exitosamente")
    time.sleep(7)
def consultarCliente():
    os.system("clear")
    print("CONSULTAR")
    nombre = input("ingrese el nombre del cliente\n")
    lista = "NOMBRE\t\tTELEFONO\n"
    with open("Directorio.txt","r") as archivo:
        for linea in archivo:
            if linea.split(",")[0] == nombre:
                lista += str(linea.split(",")[0])+"\t\t"+ str(linea.split(",")[1])+ "\n"
        print(lista)
    print("cliente consultado exitosamente")
    time.sleep(7)
def eliminarCliente():
    os.system("clear")
    print("ELIMINAR")
    nombre = input("ingrese el nombre del cliente")
    with open("Directorio.txt","r") as archivo:
        for linea in archivo:
            if linea.split(",")[0] == nombre:
                archivo.remove(linea)
                break
    print("cliente elimnado exitosamente")
    time.sleep(7)
menus = True
opc = 1
while menus == True:
    menu()
    opc = input()
    if opc == "1":
        agregarCliente()
    elif opc == "2":
        consultarCliente()
    elif opc == "3":
        eliminarCliente()
    elif opc == "0":
        menus = False