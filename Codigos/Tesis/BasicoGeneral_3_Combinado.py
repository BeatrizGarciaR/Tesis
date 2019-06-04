from math import floor

#############################
####### Lee instancia ##############
#############################
archivo = open("Instancia_Prueba_50_50_10_10_0_.txt", "r")   

productos = int(archivo.readline())
periodosTotales = int(archivo.readline())
periodos = int(archivo.readline()) 

ensambles = []
line = archivo.readline().strip().split()
for i in range(periodosTotales):
    ensambles.append(int(line[i]))

p = int(periodosTotales/periodos)
demanda = []
for i in range(productos):
    line = archivo.readline().strip().split()
    demanda.append([])
    for j in range(len(line)):
        #demanda[i].append(int(line[j]))
        demanda[i].append(int(line[j])*p*100)

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
    

a = 0
producto = []
for i in range(productos):
    producto.append(a)
    a = a + 1

cantidad =[]
for i in range(productos):
    cantidad.append(0)


periodo = 1
tipo = []
for i in range(productos):
    tipo.append(-1)


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
pasa = 0
while prodTerminados < prodTotales:
    if pasa > periodosTotales:
        #print("ENTRA 1")
        pasa = pasa + 1
        for n in range(len(producto)):
            piezas = []
            for i in range(len(tipoPiezas[vect[n]])):
                piezas.append(tipoPiezas[vect[n]][i])

            cantPiezas = []
            indPieza = []
            
            for j in range(len(tipoPiezas[vect[n]])):
                if piezas[j] in tipo:
                    indicePieza = tipo.index(piezas[j])
                    indPieza.append(indicePieza)
                    cantPiezas.append(cantidad[indicePieza])
                else:
                    indPieza.append(-1)
                    cantPiezas.append(0)

            cPiezas = []
            for k in range(len(tipoPiezas[vect[n]])):
                cPiezas.append(floor(ensambles[k]/canPiezas[vect[n]][k]))

            auxiliar = []
            for p in range(len(tipoPiezas[vect[n]])):
                if cantPiezas[p] > cPiezas[p]:
                    auxiliar.append(1)

            cuentas = auxiliar.count(1)

            
            if(cuentas == len(tipoPiezas[vect[n]])):
                #print("PASA A IF")
                for r in range(len(tipoPiezas[vect[n]])):
                    if demanda[vect[n]][1] - matrizNueva[vect[n]][r] >= cPiezas[r]:
                        if cantPiezas[r] >= cPiezas[r]*canPiezas[vect[n]][r] and cPiezas[r] != 0:
                            respuesta.append([])
                            respuesta[indice].append(periodo)
                            respuesta[indice].append(vect[n])
                            respuesta[indice].append(tipoPiezas[vect[n]][r])
                            respuesta[indice].append(cPiezas[r]*canPiezas[vect[n]][r])
                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]*canPiezas[vect[n]][r]
                            cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - cPiezas[r]*canPiezas[vect[n]][r]
                            matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + cPiezas[r]
                            indice = indice + 1
                        else:
                            varAux = floor(cantPiezas[r]/canPiezas[vect[n]][r])
                            if cantPiezas[r] >= varAux*canPiezas[vect[n]][r] and varAux != 0:
                                respuesta.append([])
                                respuesta[indice].append(periodo)
                                respuesta[indice].append(vect[n])
                                respuesta[indice].append(tipoPiezas[vect[n]][r])
                                respuesta[indice].append(varAux*canPiezas[vect[n]][r])
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[vect[n]][r]
                                cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - varAux*canPiezas[vect[n]][r]
                                matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + varAux
                                indice = indice + 1
                    else:
                        a = demanda[vect[n]][1] - matrizNueva[vect[n]][r]
                        if cantPiezas[r] >= a*canPiezas[vect[n]][r] and a != 0:
                            respuesta.append([])
                            respuesta[indice].append(periodo)
                            respuesta[indice].append(vect[n])
                            respuesta[indice].append(tipoPiezas[vect[n]][r])
                            respuesta[indice].append(a*canPiezas[vect[n]][r])
                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - a*canPiezas[vect[n]][r]
                            cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - a*canPiezas[vect[n]][r]
                            matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + a
                            indice = indice + 1
                        else:
                            varAux = floor(cantPiezas[r]/canPiezas[vect[n]][r])
                            if cantPiezas[r] >= varAux*canPiezas[vect[n]][r] and varAux != 0:
                                respuesta.append([])
                                respuesta[indice].append(periodo)
                                respuesta[indice].append(vect[n])
                                respuesta[indice].append(tipoPiezas[vect[n]][r])
                                respuesta[indice].append(varAux*canPiezas[vect[n]][r])
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[vect[n]][r]
                                cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - varAux*canPiezas[vect[n]][r]
                                matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + varAux
                                indice = indice + 1

    else:
        #print("ENTRA 2")
        for n in range(len(producto)):
            piezas = []
            for i in range(len(tipoPiezas[vect[n]])):
                piezas.append(tipoPiezas[vect[n]][i])

            cantPiezas = []
            indPieza = []
            
            for j in range(len(tipoPiezas[vect[n]])):
                if piezas[j] in tipo:
                    indicePieza = tipo.index(piezas[j])
                    indPieza.append(indicePieza)
                    cantPiezas.append(cantidad[indicePieza])
                else:
                    indPieza.append(-1)
                    cantPiezas.append(0)

            cPiezas = []
            for k in range(len(tipoPiezas[vect[n]])):
                cPiezas.append(floor(ensambles[k]/canPiezas[vect[n]][k]))

            for r in range(len(tipoPiezas[vect[n]])):
                    if demanda[vect[n]][1] - matrizNueva[vect[n]][r] >= cPiezas[r]:
                        if cantPiezas[r] >= cPiezas[r]*canPiezas[vect[n]][r] and cPiezas[r] != 0:
                            respuesta.append([])
                            respuesta[indice].append(periodo)
                            respuesta[indice].append(vect[n])
                            respuesta[indice].append(tipoPiezas[vect[n]][r])
                            respuesta[indice].append(cPiezas[r]*canPiezas[vect[n]][r])
                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]*canPiezas[vect[n]][r]
                            cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - cPiezas[r]*canPiezas[vect[n]][r]
                            matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + cPiezas[r]
                            indice = indice + 1
                        else:
                            varAux = floor(cantPiezas[r]/canPiezas[vect[n]][r])
                            if cantPiezas[r] >= varAux*canPiezas[vect[n]][r] and varAux != 0:
                                respuesta.append([])
                                respuesta[indice].append(periodo)
                                respuesta[indice].append(vect[n])
                                respuesta[indice].append(tipoPiezas[vect[n]][r])
                                respuesta[indice].append(varAux*canPiezas[vect[n]][r])
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[vect[n]][r]
                                cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - varAux*canPiezas[vect[n]][r]
                                matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + varAux
                                indice = indice + 1
                    else:
                        a = demanda[vect[n]][1] - matrizNueva[vect[n]][r]
                        if cantPiezas[r] >= a*canPiezas[vect[n]][r] and a != 0:
                            respuesta.append([])
                            respuesta[indice].append(periodo)
                            respuesta[indice].append(vect[n])
                            respuesta[indice].append(tipoPiezas[vect[n]][r])
                            respuesta[indice].append(a*canPiezas[vect[n]][r])
                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - a*canPiezas[vect[n]][r]
                            cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - a*canPiezas[vect[n]][r]
                            matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + a
                            indice = indice + 1
                        else:
                            varAux = floor(cantPiezas[r]/canPiezas[vect[n]][r])
                            if cantPiezas[r] >= varAux*canPiezas[vect[n]][r] and varAux != 0:
                                respuesta.append([])
                                respuesta[indice].append(periodo)
                                respuesta[indice].append(vect[n])
                                respuesta[indice].append(tipoPiezas[vect[n]][r])
                                respuesta[indice].append(varAux*canPiezas[vect[n]][r])
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[vect[n]][r]
                                cantidadPiezas[vect[n]][r] = cantidadPiezas[vect[n]][r] - varAux*canPiezas[vect[n]][r]
                                matrizNueva[vect[n]][r] = matrizNueva[vect[n]][r] + varAux
                                indice = indice + 1
                
    
    for k in range(len(piezasPeriodo)): 
        if piezasPeriodo[k][0] <= periodo:
            if piezasPeriodo[k][1] not in tipo:
                tipo[piezasPeriodo[k][1]] = piezasPeriodo[k][1]
                ind = tipo.index(piezasPeriodo[k][1])
                cantidad[ind] = cantidad[ind] + piezasPeriodo[k][2]
            else:
                ind = tipo.index(piezasPeriodo[k][1])
                cantidad[ind] = cantidad[ind] + piezasPeriodo[k][2]
            piezasPeriodo[k][0] = 1000000

    periodo = periodo + 1
    if periodo > periodosTotales + floor((5/2)*periodosTotales):
        break 

    prodTerminados = 0
    for i in range(productos):
        minimo = min(matrizNueva[i])
        prodTerminados = prodTerminados + minimo
        

sumar = 0
sumar = sum(cantidad)

productosDemanda = []
for i in range(productos):
    minimo = min(matrizNueva[i])
    if minimo == demanda[i][1]:
        productosDemanda.append(i)

print("cantidad")
print(cantidad)
print("productos terminados")
print(prodTerminados)
print("piezas en almacen")
print(sumar)
    
with open("Respuesta_50_50_10_10_0_.txt", "w") as crear:
    print(productosDemanda, file=crear)
    for k in range(len(respuesta)):
        if len(respuesta[k]) > 1 :
            l = respuesta[k]
            a = " ".join(str(i) for i in l)
            print(a, file=crear)
    for i in range(len(matrizNueva)):
        print(i, matrizNueva[i], file=crear)
    

