import json
import os
import time

ruta = "AutoShopping.json"
with open(ruta,"r") as archivo:
    biblioteca = json.load(archivo)

def guardar():
    with open(ruta,"w") as archivo:
        json.dump(biblioteca,archivo,indent=4)
def mostrarColumna():
    contador = 1
    print("ID"+"\t"+"MARCA"+"\t\t"+"LINEA"+"\t\t"+"MODELO"+"\t\t"+"PRECIO"+"\t\t"+"EQUIPAMIENTO\n")

    for i in range(len(biblioteca["autostore"]["auto"])):
        print(str(contador)+"\t"+str(biblioteca["autostore"]["auto"][i]["marca"]).ljust(15-len(biblioteca["autostore"]["auto"][i]["marca"]))+"\t" + \
                str(biblioteca["autostore"]["auto"][i]["linea"]).ljust(15-len(biblioteca["autostore"]["auto"][i]["linea"]))+"\t" + \
                str(biblioteca["autostore"]["auto"][i]["modelo"]).ljust(15-len(biblioteca["autostore"]["auto"][i]["modelo"]))+"\t" + \
                str(biblioteca["autostore"]["auto"][i]["precio"]).ljust(15-len(biblioteca["autostore"]["auto"][i]["precio"]))+"\t" + \
                str(biblioteca["autostore"]["auto"][i]["equipamiento"]).ljust(15-len(biblioteca["autostore"]["auto"][i]["equipamiento"])) + "\n")
        contador += 1
def mostrarTitulos():
    contador = 1
    print("ID"+"\t\t"+"MARCA\n")
    for i in range(len(biblioteca["autostore"]["auto"])):
        print(str(contador)+"\t\t"+str(biblioteca["autostore"]["auto"][i]["marca"]))
        contador += 1

def mostrarTodo(id):
    equipamiento = ""
    if type(biblioteca["autostore"]["auto"][id-1]["equipamiento"]) == list:
        for i in biblioteca["autostore"]["auto"][id-1]["equipamiento"]:
            equipamiento += str(i)+ "\n"
    else:
        equipamiento = biblioteca["autostore"]["auto"][id-1]["equipamiento"]
    os.system("clear")
    print("VISTA***")
    print("linea: "+biblioteca["autostore"]["auto"][id-1]["linea"] +"\n" \
        "modelo: "+biblioteca["autostore"]["auto"][id-1]["modelo"] +"\n" \
        "precio: "+biblioteca["autostore"]["auto"][id-1]["precio"]+"\n" \
        "equipamiento: "+ "\n" + equipamiento + "\n")
    return

def varios():
    seguir = True
    equipamiento=[]
    while seguir == True:
        añadir = input("Ingrese el euipamiento:")
        op = input("Desea agregar otro euipamiento?\nS:si\nN:no\n")
        equipamiento.append(añadir)
        if op.lower() == "n":
            seguir = False
    return equipamiento

def create():
    marca = input("Ingrese la marca:\n")
    linea = input("Ingrese la linea :\n")
    modelo = input("Ingrese el modelo:\n")
    precio = input("Ingrese el precio:\n")
    equipamientos = int(input("desea agregar un equipamientos o mas ?\n1. solo uno\2.2.varios\n"))
    if equipamientos == 1:
        equipamiento = input("Ingrese el equipamientos:\n")
    else:
        equipamiento = varios()
    auto = {
        "marca": marca,
        "linea": linea,
        "modelo": modelo,
        "precio": precio,
        "equipamiento": equipamiento
    }
    biblioteca["autostore"]["auto"].append(auto)
    guardar()
    return
def update():
    os.system("clear")
    mostrarTitulos()
    codigo = int(input("que auto desea actualizar?:\n"))
    for i in range(len(biblioteca["autostore"]["auto"])+1):
        if codigo == i:
            mostrarTodo(codigo)
            m = int(input("que desea modificar?\n1.marca\n2.linea\n3.modelo\n4.precio\n5.equipamiento\n"))
            if m == 1:
                marca = input("Ingrese la marca:\n\n")
                biblioteca["autostore"]["auto"][codigo-1]["marca"]= marca
            elif m == 2:
                linea = input("Ingrese la linea:\n")
                biblioteca["autostore"]["auto"][codigo-1]["linea"] = linea
            elif m == 3:           
                modelo = input("Ingrese el modelo:\n")
                biblioteca["autostore"]["auto"][codigo-1]["modelo"] = modelo
            elif m == 4:        
                precio = input("Ingrese el precio:\n")
                biblioteca["autostore"]["auto"][codigo-1]["precio"] = precio
            elif m == 5:
                if type(biblioteca["autostore"]["auto"][codigo-1]["equipamiento"]) is str:
                    equipamiento = input("Ingrese el equipamiento:\n")
                    biblioteca["autostore"]["auto"][codigo-1]["equipamiento"] = equipamiento
                else:
                    print(biblioteca["autostore"]["auto"][codigo-1]["equipamiento"])
                    saber = input("Ingrese el equipamiento en especifico a editar:\n")
                    for i in range(len(biblioteca["autostore"]["auto"][codigo-1]["equipamiento"])):
                        if saber == biblioteca["autostore"]["auto"][codigo-1]["equipamiento"][i]:
                            equipamiento = input("Ingrese el nuevo equipamiento:\n")
                            biblioteca["autostore"]["auto"][codigo-1]["equipamiento"][i] = equipamiento
                            break
            else:
                print("VALOR EQUIVOCADO")
    guardar()
    return

def delete():
    mostrarTitulos()
    codigo = int(input("que auto desea eliminar?:\n"))
    for i in range(len(biblioteca["autostore"]["auto"])+1):
        if codigo == i:
            biblioteca["autostore"]["auto"].pop(codigo-1)
    guardar()
    return

def menu():
    os.system("clear")
    print("""Bienvenido al menu de autos\n
        1. Mostrar en pantalla todos los automóviles a la venta 
        2. Crear Nuevo Auto 
        3. Mostrar los datos de Autos consultado por Marca 
        4. Actualizar los datos de un Auto 
        5. Eliminar un Auto 
        0. salir\n""")
def mostrarMarca():
    marca=input("Ingrese la marca del auto: ")
    marcaD={}
    id=1
    for i in range(len(biblioteca["autostore"]["auto"])):
        if biblioteca["autostore"]["auto"][i]["marca"]==marca:
            marcaD[id]=biblioteca["autostore"]["auto"][i]
            id +=1
    listaMarca="Id\tMarca\t\tLinea\t\tModelo\t\tPrecio\t\tEquipamiento"
    for i in marcaD:
        listaMarca=listaMarca+"\n"+str(i)+"\t"+str(marcaD[i]["marca"]).ljust(15-len(str(marcaD[i]["marca"])))+"\t"+str(marcaD[i]["linea"]).ljust(15-len(str(marcaD[i]["linea"])))+"\t"+str(marcaD[i]["modelo"]).ljust(15-len(str(marcaD[i]["modelo"])))+"\t"+str(marcaD[i]["precio"]).ljust(15-len(str(marcaD[i]["precio"])))+"\t"+str(marcaD[i]["equipamiento"]).ljust(15-len(str(marcaD[i]["equipamiento"])))+"\n"
        id +=1
    print(listaMarca)
    return
seguir = True
while seguir == True:
    menu()
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        mostrarColumna()
        time.sleep(7)
    elif opcion == 2:
        create()
    elif opcion == 3:
        os.system("clear")
        mostrarMarca()
        time.sleep(7)
    elif opcion == 4:
        update()
    elif opcion == 5:
        os.system("clear")
        delete()
    elif opcion == 0:
        seguir = False
    else:
        print("Opcion no valida")
