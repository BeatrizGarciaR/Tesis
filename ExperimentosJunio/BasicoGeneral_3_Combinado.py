from math import floor
import random
    ##
numMaquinas = [10,20,30]
numInst = [0,1,2,3,5,6,7,9]

for iteracion in numMaquinas:
    for itera in numInst:
        for iteraciones in range(5):

    #############################
    ####### Lee instancia ##############
    #############################
    #archivo = open("Instancia_Prueba_50_50_10_10_"+str(itera)+"_"+str(iteracion+1)+".txt", "r")   
            archivo = open("Instancia_Prueba_50_50_10_" + str(iteracion) + "_" + str(itera) + ".txt", "r")   
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
                if pasa < floor((4/5)*periodosTotales):
                    #print("ENTRA 1")
                    pasa = pasa + 1
                    rcl = []
                    while len(rcl) < floor(len(producto)/3):
                        aleatorio = random.randrange(0,50,1)
                        if aleatorio not in rcl:
                           rcl.append(aleatorio)
                           
                    for n in range(len(rcl)):
                        piezas = []
                        for i in range(len(tipoPiezas[rcl[n]])):
                            piezas.append(tipoPiezas[rcl[n]][i])

                        cantPiezas = []
                        indPieza = []
                        
                        for j in range(len(tipoPiezas[rcl[n]])):
                            if piezas[j] in tipo:
                                indicePieza = tipo.index(piezas[j])
                                indPieza.append(indicePieza)
                                cantPiezas.append(cantidad[indicePieza])
                            else:
                                indPieza.append(-1)
                                cantPiezas.append(0)

                        cPiezas = []
                        for k in range(len(tipoPiezas[rcl[n]])):
                            cPiezas.append(floor(ensambles[k]/canPiezas[rcl[n]][k]))

                        auxiliar = []
                        for p in range(len(tipoPiezas[rcl[n]])):
                            if cantPiezas[p] > cPiezas[p]:
                                auxiliar.append(1)

                        cuentas = auxiliar.count(1)

                        
                        if(cuentas == len(tipoPiezas[rcl[n]])):
                            #print("PASA A IF")
                            for r in range(len(tipoPiezas[rcl[n]])):
                                if demanda[rcl[n]][1] - matrizNueva[rcl[n]][r] > cPiezas[r]:
                                    if cantPiezas[r] >= cPiezas[r]*canPiezas[rcl[n]][r] and cPiezas[r] != 0:
                                        respuesta.append([])
                                        respuesta[indice].append(periodo)
                                        respuesta[indice].append(rcl[n])
                                        respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                        respuesta[indice].append(cPiezas[r]*canPiezas[rcl[n]][r])
                                        cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]*canPiezas[rcl[n]][r]
                                        cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - cPiezas[r]*canPiezas[rcl[n]][r]
                                        matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + cPiezas[r]
                                        indice = indice + 1
                                    else:
                                        varAux = floor(cantPiezas[r]/canPiezas[rcl[n]][r])
                                        if cantPiezas[r] >= varAux*canPiezas[rcl[n]][r] and varAux != 0:
                                            respuesta.append([])
                                            respuesta[indice].append(periodo)
                                            respuesta[indice].append(rcl[n])
                                            respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                            respuesta[indice].append(varAux*canPiezas[rcl[n]][r])
                                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[rcl[n]][r]
                                            cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - varAux*canPiezas[rcl[n]][r]
                                            matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + varAux
                                else:
                                    a = demanda[rcl[n]][1] - matrizNueva[rcl[n]][r]
                                    if cantPiezas[r] >= a*canPiezas[rcl[n]][r] and a != 0:
                                        respuesta.append([])
                                        respuesta[indice].append(periodo)
                                        respuesta[indice].append(rcl[n])
                                        respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                        respuesta[indice].append(a*canPiezas[rcl[n]][r])
                                        cantidad[indPieza[r]] = cantidad[indPieza[r]] - a*canPiezas[rcl[n]][r]
                                        cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - a*canPiezas[rcl[n]][r]
                                        matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + a
                                        indice = indice + 1
                                    else:
                                        varAux = floor(cantPiezas[r]/canPiezas[rcl[n]][r])
                                        if cantPiezas[r] >= varAux*canPiezas[rcl[n]][r] and varAux != 0:
                                            respuesta.append([])
                                            respuesta[indice].append(periodo)
                                            respuesta[indice].append(rcl[n])
                                            respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                            respuesta[indice].append(varAux*canPiezas[rcl[n]][r])
                                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[rcl[n]][r]
                                            cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - varAux*canPiezas[rcl[n]][r]
                                            matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + varAux

                else:
                    #print("ENTRA 2")
                    rcl = []
                    while len(rcl) < floor(len(producto)/3):
                        aleatorio = random.randrange(0,50,1)
                        if aleatorio not in rcl:
                           rcl.append(aleatorio)
                           
                    for n in range(len(rcl)):
                        piezas = []
                        for i in range(len(tipoPiezas[rcl[n]])):
                            piezas.append(tipoPiezas[rcl[n]][i])

                        cantPiezas = []
                        indPieza = []
                        
                        for j in range(len(tipoPiezas[rcl[n]])):
                            if piezas[j] in tipo:
                                indicePieza = tipo.index(piezas[j])
                                indPieza.append(indicePieza)
                                cantPiezas.append(cantidad[indicePieza])
                            else:
                                indPieza.append(-1)
                                cantPiezas.append(0)

                        cPiezas = []
                        for k in range(len(tipoPiezas[rcl[n]])):
                            cPiezas.append(floor(ensambles[k]/canPiezas[rcl[n]][k]))

                        for r in range(len(tipoPiezas[rcl[n]])):
                                if demanda[rcl[n]][1] - matrizNueva[rcl[n]][r] > cPiezas[r]:
                                    if cantPiezas[r] >= cPiezas[r]*canPiezas[rcl[n]][r] and cPiezas[r] != 0:
                                        respuesta.append([])
                                        respuesta[indice].append(periodo)
                                        respuesta[indice].append(rcl[n])
                                        respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                        respuesta[indice].append(cPiezas[r]*canPiezas[rcl[n]][r])
                                        cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]*canPiezas[rcl[n]][r]
                                        cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - cPiezas[r]*canPiezas[rcl[n]][r]
                                        matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + cPiezas[r]
                                        indice = indice + 1
                                    else:
                                        varAux = floor(cantPiezas[r]/canPiezas[rcl[n]][r])
                                        if cantPiezas[r] >= varAux*canPiezas[rcl[n]][r] and varAux != 0:
                                            respuesta.append([])
                                            respuesta[indice].append(periodo)
                                            respuesta[indice].append(rcl[n])
                                            respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                            respuesta[indice].append(varAux*canPiezas[rcl[n]][r])
                                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[rcl[n]][r]
                                            cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - varAux*canPiezas[rcl[n]][r]
                                            matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + varAux
                                else:
                                    a = demanda[rcl[n]][1] - matrizNueva[rcl[n]][r]
                                    if cantPiezas[r] >= a*canPiezas[rcl[n]][r] and a != 0:
                                        respuesta.append([])
                                        respuesta[indice].append(periodo)
                                        respuesta[indice].append(rcl[n])
                                        respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                        respuesta[indice].append(a*canPiezas[rcl[n]][r])
                                        cantidad[indPieza[r]] = cantidad[indPieza[r]] - a*canPiezas[rcl[n]][r]
                                        cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - a*canPiezas[rcl[n]][r]
                                        matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + a
                                        indice = indice + 1
                                    else:
                                        varAux = floor(cantPiezas[r]/canPiezas[rcl[n]][r])
                                        if cantPiezas[r] >= varAux*canPiezas[rcl[n]][r] and varAux != 0:
                                            respuesta.append([])
                                            respuesta[indice].append(periodo)
                                            respuesta[indice].append(rcl[n])
                                            respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                            respuesta[indice].append(varAux*canPiezas[rcl[n]][r])
                                            cantidad[indPieza[r]] = cantidad[indPieza[r]] - varAux*canPiezas[rcl[n]][r]
                                            cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - varAux*canPiezas[rcl[n]][r]
                                            matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + varAux
                            
                
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
                if periodo > periodosTotales + floor((1/4)*periodosTotales):
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

            productosMinimos = []
            for i in range(productos):
                minimo = min(matrizNueva[i])
                if minimo > 0 :
                    productosMinimos.append(i)

            #print("cantidad")
            #print(cantidad)
            print("Iteracion", iteracion, itera, iteraciones)
            print("productos terminados")
            print(prodTerminados)
            print("piezas en almacen")
            print(sumar)
                
            #with open("Respuesta_50_50_10_10_"+str(itera)+"_"+str(iteracion+1)+".txt", "w") as crear:
            with open("Periodos3_50_50_10_" + str(iteracion) + "_" + str(itera) + "_" + str(iteraciones+1) + ".txt", "w") as crear:
                #print(productosDemanda, file=crear)
                for k in range(len(respuesta)):
                    if len(respuesta[k]) > 0:
                        print(respuesta[k][0], respuesta[k][1], respuesta[k][2], respuesta[k][3], file=crear)

            with open("InfLE3_50_50_10_" + str(iteracion) + "_" + str(itera) + "_" + str(iteraciones+1) + ".txt", "w") as nuevo:
                print(periodos, file=nuevo)
                print(periodo, file=nuevo)
                print(sumar, file=nuevo)
                print(prodTerminados, file=nuevo)
                print(productosMinimos, file=nuevo)
                print(productosDemanda, file=nuevo)
                
                for i in range(len(matrizNueva)):
                    print(min(matrizNueva[i]), i, matrizNueva[i], file=nuevo)
                

