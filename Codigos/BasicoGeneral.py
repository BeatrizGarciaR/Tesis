#############################
####### Lee instancia ##############
#############################
archivo = open("Instancia_2.txt", "r")   
     
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

utilizado = []
for i in range(productos*columnas):
    utilizado.append(0)

periodo = 1
prodTerminado = 0
tipo = []
finEnsamble = []
inicioEnsamble = []

#############################
####### Corre programa ############
#############################

while prodTerminado < len(producto):
    print("Periodo = ", periodo)
    for n in range(productos):
        if producto[n] is not 0:
            piezas = []
            for i in range(columnas):
                piezas.append(tipoPiezas[n][i])

            cantPiezas = []
            indPieza = []
            for j in range(columnas):
                if piezas[j] in tipo:
                    indicePieza = tipo.index(piezas[j])
                    indPieza.append(indicePieza)
                    cantPiezas.append(cantidad[indicePieza])
                else:
                    indPieza.append(-1)
                    cantPiezas.append(0)

            cPiezas = []
            for k in range(columnas):
                cPiezas.append(cantidadPiezas[n][k])
                
            if cantPiezas[0] >= cPiezas[0] or producto[n] in utilizado:
                contPiezas = 0
                for r in range(columnas):                           
                    if cantPiezas[r] >= cPiezas[r] and producto[n] != utilizado[(columnas)*producto[n] - (columnas-r)]:
                        contPiezas = contPiezas + 1
                        if r != 0:
                            inicioEnsamble.append(periodo)
                        while cPiezas[r] > 0:
                            if cPiezas[r] < ensambles[r]:
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]
                                cPiezas[r] = 0
                                cantidadPiezas[n][r] = 0
                            else:
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - ensambles[r]
                                cPiezas[r] = cPiezas[r] - ensambles[r]
                                cantidadPiezas[n][r] = cantidadPiezas[n][r] - ensambles[r]
                                periodo = periodo + 1
                        if r != 0:
                            finEnsamble.append(periodo)
                        utilizado[(columnas)*producto[n] - (columnas-r)] = producto[n]
            
                cdp = 0
                cdp = utilizado.count(producto[n])
                if cdp == columnas:
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
