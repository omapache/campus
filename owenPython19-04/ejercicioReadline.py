archivoTexto = open("nombres.txt","r")
archivo = archivoTexto.readlines()
archivoTexto.close()
print(archivo)
for i in range(len(archivo)):
    print("nombre:", archivo[i])