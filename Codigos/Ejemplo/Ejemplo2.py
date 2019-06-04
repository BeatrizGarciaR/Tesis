archivo = open("Instancia1.txt", "r")
matriz = []
for i in range(4):
    line = archivo.readline()
    matriz.append([])
    for j in range(5):
        matriz[i].append(int(line[j*2]))
print(matriz)
archivo.close()

