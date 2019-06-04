#############################
####### Lee instancia ##############
#############################
archivo = open("Instancia_1.txt", "r")   
     
cantidadPiezas = []
productos = int(archivo.readline())
columnas = int(archivo.readline())

ensambles = []
line = archivo.readline().strip().split()
for i in range(columnas):
    ensambles.append(int(line[i]))

for i in range(productos):
    line = archivo.readline().strip().split()
    cantidadPiezas.append([])
    for j in range(columnas):
        cantidadPiezas[i].append(int(line[j]))

tipoPiezas = []
for i in range(productos):
    line = archivo.readline().strip().split()
    tipoPiezas.append([])
    for j in range(int(columnas)):
        tipoPiezas[i].append(int(line[j]))

piezasPeriodo = []
columna = int(archivo.readline())
linea = archivo.readline().strip().split()
i = 0
num = 0
while int(linea[0]) is not -1:
    piezasPeriodo.append([])
    for j in range(columna):
        piezasPeriodo[i].append(int(linea[j]))
    linea = archivo.readline().strip().split()
    i = i + 1
    num = num + 1

archivo.close()


#############################
####### Declaracion var. ############
#############################

a = 0
producto = []
for i in range(productos):
    a = a + 1
    producto.append(a)

cantidad = []
aux = []
for i in range(len(piezasPeriodo)):
    for j in range(len(piezasPeriodo)):
        if piezasPeriodo[i][1] != piezasPeriodo[j][1]:
            if piezasPeriodo[i][1] not in aux:
                cantidad.append(0)
                aux.append(piezasPeriodo[i][1])

periodo = 1
prodTerminado = 0
tipo = []
finEnsamble = []
inicioEnsamble = []
cuerposUsados = []
brazosUsados = []
piernasUsados = []
cabezasUsados = []

#############################
####### Corre programa ############
#############################

while prodTerminado < len(producto):
    print("Periodo = ", periodo)
    for n in range(productos):
        if producto[n] is not 0:
            cuerpo = tipoPiezas[n][0]
            brazo = tipoPiezas[n][1]
            cabeza = tipoPiezas[n][2]
            pierna = tipoPiezas[n][3]
            if cuerpo in tipo:
                ind1 = tipo.index(cuerpo)
                cantCuerpo = cantidad[ind1]
            else:
                cantCuerpo = 0
            if brazo in tipo:
                ind2 = tipo.index(brazo)
                cantBrazo = cantidad[ind2]
            else:
                cantBrazo = 0
            if pierna in tipo:
                ind3 = tipo.index(pierna)
                cantPierna = cantidad[ind3]
            else:
                cantPierna = 0
            if cabeza in tipo:
                ind4 = tipo.index(cabeza)
                cantCabeza = cantidad[ind4]
            else:
                cantCabeza = 0

            cCuerpo= cantidadPiezas[n][0]
            cBrazo = cantidadPiezas[n][1]
            cCabeza = cantidadPiezas[n][2]
            cPierna = cantidadPiezas[n][3]
            if cantCuerpo >= cCuerpo or producto[n] in cuerposUsados:
                contPiezas = 0
                if cantBrazo >= cBrazo and producto[n] not in brazosUsados:
                    contPiezas = contPiezas + 1
                    inicioEnsamble.append(periodo)
                    while cBrazo > 0:
                        if cBrazo < ensambles[1]:
                            cantidad[ind2] = cantidad[ind2] - cBrazo
                            cBrazo = 0
                            cantidadPiezas[n][1] = 0
                        else:
                            cantidad[ind2] = cantidad[ind2] - ensambles[1]
                            cBrazo = cBrazo - ensambles[1]
                            cantidadPiezas[n][1] = cantidadPiezas[n][1] - ensambles[1]
                            periodo = periodo + 1
                    finEnsamble.append(periodo)
                    brazosUsados.append(producto[n])
                if cantPierna >= cPierna and producto[n] not in piernasUsados:
                    contPiezas = contPiezas + 1
                    inicioEnsamble.append(periodo)
                    while cPierna > 0:
                        if cPierna < ensambles[3]:
                            cantidad[ind3] = cantidad[ind3] - cPierna
                            cPierna = 0
                            cantidadPiezas[n][3] = 0
                        else:
                            cantidad[ind3] = cantidad[ind3] - ensambles[3]
                            cPierna = cPierna - ensambles[3]
                            cantidadPiezas[n][3] = cantidadPiezas[n][3] - ensambles[3]
                            periodo = periodo + 1
                    finEnsamble.append(periodo)
                    piernasUsados.append(producto[n])
                if cantCabeza >= cCabeza and producto[n] not in cabezasUsados:
                    contPiezas = contPiezas + 1
                    inicioEnsamble.append(periodo)
                    while cCabeza > 0:
                         if cCabeza < ensambles[2]:
                            cantidad[ind4] = cantidad[ind4] - cCabeza
                            cCabeza = 0
                            cantidadPiezas[n][2] = 0
                         else:
                            cantidad[ind4] = cantidad[ind4] - ensambles[2]
                            cCabeza = cCabeza - ensambles[2]
                            cantidadPiezas[n][2] = cantidadPiezas[n][2] - ensambles[2]
                    finEnsamble.append(periodo)
                    cabezasUsados.append(producto[n])
                if contPiezas > 0 and producto[n] not in cuerposUsados:
                    cuerposUsados.append(producto[n])
                    while cCuerpo > 0:
                        if cCuerpo < ensambles[0]:
                            cantidad[ind1] = cantidad[ind1] - cCuerpo
                            cCuerpo = 0
                            cantidadPiezas[n][0] = 0
                        else:
                            cantidad[ind1] = cantidad[ind1] - ensambles[0]
                            cCuerpo = cCuerpo - ensambles[3] 
                            cantidadPiezas[n][0] = cantidadPiezas[n][0] - ensambles[0]
                print("Producto", producto[n])
                cdp = 0
                if producto[n]  in brazosUsados:
                    cdp = cdp + 1
                if producto[n]  in piernasUsados:
                    cdp = cdp + 1
                if producto[n]  in cabezasUsados:
                    cdp = cdp + 1
                if cdp == 3:
                    producto[n] = 0
                prodTerminado = 0
                for i in range(len(producto)):
                    if producto[i] == 0:
                        prodTerminado = prodTerminado + 1
                break #indica que en el mismo periodo no puede ensamblarse mas de un tipo de producto

    for k in range(len(piezasPeriodo)): 
        if piezasPeriodo[k][0] <= periodo:
            if piezasPeriodo[k][1] not in tipo:
                tipo.append(piezasPeriodo[k][1])
                ind = tipo.index(piezasPeriodo[k][1])
                cantidad[ind] = cantidad[ind] + piezasPeriodo[k][2]
            else:
                ind = tipo.index(piezasPeriodo[k][1])
                cantidad[ind] = cantidad[ind] + piezasPeriodo[k][2]
            piezasPeriodo[k][0] = 1000000

    periodo = periodo + 1
    if periodo > 20:
        break
    print("Productos terminados", prodTerminado)
print("Periodo del inicio del ensamble de cada producto:", inicioEnsamble)
print("Periodo del término de ensamble de cada producto: ", finEnsamble)
            
                
            
                    
                
                    










                        
