archivo = open("Instancia1.txt", "r")
matriz = []
filas = int(archivo.readline())
columnas = int(archivo.readline())
for i in range(filas):
    line = archivo.readline()
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(int(line[j*2]))
print(matriz)
archivo.close()
