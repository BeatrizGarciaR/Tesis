import csv 

with open("Instancia1.txt", newline="") as leer:

    archivo = csv.reader(leer, delimiter=" ")
    while 
        
cantidadPiezas = []
productos = int(archivo.readline())
columnas = int(archivo.readline())
for i in range(int(productos)):
    line = archivo.readline()
    cantidadPiezas.append([])
    for j in range(int(columnas)):
        if line[j] != " " :
            cantidadPiezas[i].append(int(line[j]))
print(cantidadPiezas)

tipoPiezas = []
for i in range(int(productos)):
    line = archivo.readline()
    tipoPiezas.append([])
    for j in range(int(columnas)):
        tipoPiezas[i].append(int(line[j]))
print(tipoPiezas)

columna = int(archivo.readline())
piezasPeriodo = []
linea = archivo.readline()
i = 0
while linea != -1:
    linea = archivo.readline()
    piezasPeriodo.append([])
    for j in range(int(columna)):
        piezasPeriodo[i].append(int(linea[j]))
    i = i + 1
print(piezasPeriodo)

archivo.close()
