
from math import floor

#############################
####### Lee instancia ##############
#############################
archivo = open("Instancia_Prueba_50_50_10_10_0_.txt", "r")   

productos = int(archivo.readline())
horas = int(archivo.readline())
periodos = int(archivo.readline()) 

ensambles = []
line = archivo.readline().strip().split()
for i in range(horas):
    ensambles.append(int(line[i]))

p = int(horas/periodos)
demanda = []
for i in range(productos):
    line = archivo.readline().strip().split()
    demanda.append([])
    for j in range(len(line)):
        demanda[i].append(int(line[j])*p*100)
        #demanda[i].append(int(line[j]))

preferencia = []
for i in range(productos):
    line = archivo.readline().strip().split()
    preferencia.append([])
    for j in range(len(line)):
        preferencia[i].append(int(line[j]))


cantidadPiezas = []
for i in range(productos):
    line = archivo.readline().strip().split()
    cantidadPiezas.append([])
    for j in range(len(line)):
        cantidadPiezas[i].append(int(line[j])*demanda[i][1])

canPiezas = []
for i in range(productos):
    canPiezas.append([])
    for j in range(len(cantidadPiezas[i])):
        canPiezas[i].append(int(cantidadPiezas[i][j]/demanda[i][1]))


##print(demanda)
##print("preferencia")
##print(preferencia)
        
tipoPiezas = []
for i in range(productos):
    line = archivo.readline().strip().split()
    tipoPiezas.append([])
    for j in range(len(line)):
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

vect = []
for i in range(len(preferencia)):
    vect.append(preferencia[i][0])

##print("vector")
##print(vect)

a = 0
producto = []
for i in range(productos):
    producto.append(a)
    a = a + 1

cantidad = []
aux = []
for i in range(len(piezasPeriodo)):
    for j in range(len(piezasPeriodo)):
        if piezasPeriodo[i][1] != piezasPeriodo[j][1]:
            if piezasPeriodo[i][1] not in aux:
                cantidad.append(0)
                aux.append(piezasPeriodo[i][1])

periodo = 1
tipo = []

matrizNueva = []
for i in range(productos):
    matrizNueva.append([])
    for j in range(len(tipoPiezas[i])):
        matrizNueva[i].append(0)

prodTotales = 0
for i in range(productos):
    prodTotales = prodTotales + demanda[i][1]

#############################
####### Corre programa ############
#############################
indice = 0
respuesta = []
prodTerminados = 0
while prodTerminados < prodTotales:
    for n in range(len(producto)):
        piezas = []
        for i in range(len(tipoPiezas[producto[n]])):
            piezas.append(tipoPiezas[producto[n]][i])

        cantPiezas = []
        indPieza = []
        for j in range(len(tipoPiezas[producto[n]])):
            if piezas[j] in tipo:
                indicePieza = tipo.index(piezas[j])
                indPieza.append(indicePieza)
                cantPiezas.append(cantidad[indicePieza])
            else:
                indPieza.append(-1)
                cantPiezas.append(0)

        cPiezas = []
        for k in range(len(tipoPiezas[producto[n]])):
            cPiezas.append(floor(ensambles[k]/canPiezas[producto[n]][k]))
            
            
        for r in range(len(tipoPiezas[producto[n]])):
            if demanda[producto[n]][1] - matrizNueva[producto[n]][r] > cPiezas[r]:
                if cantPiezas[r] >= cPiezas[r]*canPiezas[producto[n]][r]:
                    respuesta.append([])
                    respuesta[indice].append(periodo)
                    respuesta[indice].append(producto[producto[n]])
                    respuesta[indice].append(tipoPiezas[producto[n]][r])
                    respuesta[indice].append(cPiezas[r]*canPiezas[producto[n]][r])
                    cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]*canPiezas[producto[n]][r]
                    cantidadPiezas[producto[n]][r] = cantidadPiezas[producto[n]][r] - cPiezas[r]*canPiezas[producto[n]][r]
                    matrizNueva[producto[n]][r] = matrizNueva[producto[n]][r] + cPiezas[r]
                    indice = indice + 1
            else:
                a = demanda[producto[n]][1] - matrizNueva[producto[n]][r]
                if cantPiezas[r] >= a*canPiezas[producto[n]][r] and a != 0:
                    respuesta.append([])
                    respuesta[indice].append(periodo)
                    respuesta[indice].append(producto[producto[n]])
                    respuesta[indice].append(tipoPiezas[producto[n]][r])
                    respuesta[indice].append(a*canPiezas[producto[n]][r])
                    cantidad[indPieza[r]] = cantidad[indPieza[r]] - a*canPiezas[producto[n]][r]
                    cantidadPiezas[producto[n]][r] = cantidadPiezas[producto[n]][r] - a*canPiezas[producto[n]][r]
                    matrizNueva[producto[n]][r] = matrizNueva[producto[n]][r] + a
                    indice = indice + 1

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
    if periodo > 2500:
        break 

    prodTerminados = 0
    for i in range(productos):
        minimo = min(matrizNueva[i])
        prodTerminados = prodTerminados + minimo
        

productosDemanda = []
for i in range(productos):
    minimo = min(matrizNueva[i])
    if minimo == demanda[i][1]:
        productosDemanda.append(i)
    
with open("Respuesta_50_50_10_10_0_2_.txt", "w") as crear:
    print(productosDemanda, file=crear)
    for k in range(len(respuesta)):
        print(respuesta[k][0], respuesta[k][1], respuesta[k][2], respuesta[k][3], file=crear)
    for i in range(len(matrizNueva)):
        print(i, matrizNueva[i], file=crear)
    
print("cantidad")
print(cantidad)
print("productos terminados")
print(prodTerminados)
