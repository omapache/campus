import json
import os
ruta = "crud.json"
empresa = {
    "cliente":[]
}
if not os.path.exists(ruta):
    with open(ruta,"w") as archivo:
        json.dump(empresa,archivo,indent=4)
        
with open("crud.json","r") as archivo:
    crud = json.load(archivo)
    archivo.close()

def agregarid():
    id = len(crud["cliente"])
    return id + 1

def agregar():
    id = agregarid()
    crud["cliente"].append({
        "id":id,
        "nombre":input("ingrese el nombre de la persona:\n"),
        "edad": input("ingrese la edad de la persona:\n"),
        "numdoc":input("ingrese el numero de documento de la persona:\n")
    })
#agregar()
def read():
    lista = "ID\t\tNOMBRE\t\tEDAD\t\tNUMERO DE DOCUMENTO\n"
    for i in range(len(crud["cliente"])):
        lista += str(crud["cliente"][i]["id"]) +"\t\t"+ \
                str(crud["cliente"][i]["nombre"])+"\t\t"+ \
                str(crud["cliente"][i]["edad"])+"\t\t" + \
                str(crud["cliente"][i]["numdoc"])+"\t\t" + "\n"
        print(lista)
read()
with open("crud.json","w") as archivo:
    json.dump(crud,archivo,indent=4)
