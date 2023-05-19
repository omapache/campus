import json
dict = {"1":"lapiz",
        "2":"borrador",
        "3":"cuaderno",
        "4":"lapicero"}
with open("jsonsito.json","w") as archivo:
    json.dump(dict,archivo)
    archivo.close()
with open("jsonsito.json","r") as archivo:
    diccionario = json.load(archivo)
    archivo.close()
llave = input("ingrese el numero :")
print(diccionario[llave])
