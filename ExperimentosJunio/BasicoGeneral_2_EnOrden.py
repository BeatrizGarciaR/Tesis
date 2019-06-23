
from math import floor
import random 

#############################
####### Lee instancia ##############
#############################

numMaquinas = [10,20,30]
numInst = [0,1,2,3,5,6,7,9]

for iteracion in numMaquinas:
    for itera in numInst:
        for iteraciones in range(5):

            archivo = open("Instancia_Prueba_50_50_10_" + str(iteracion) + "_" + str(itera) +   ".txt", "r")   

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


producto1=[i for i in range(productos)]
print(producto1)

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

                rcl = []
                while len(rcl) < floor(len(producto)/3):
                    aleatorio = random.randrange(0,50,1)
                    if aleatorio not in rcl:
                       rcl.append(aleatorio)
                #print(rcl)

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
                            if cantPiezas[r] >= cPiezas[r]*canPiezas[rcl[n]][r]:
                                respuesta.append([])
                                respuesta[indice].append(periodo)
                                respuesta[indice].append(producto[rcl[n]])
                                respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                respuesta[indice].append(cPiezas[r]*canPiezas[rcl[n]][r])
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - cPiezas[r]*canPiezas[rcl[n]][r]
                                cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - cPiezas[r]*canPiezas[rcl[n]][r]
                                matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + cPiezas[r]
                                indice = indice + 1
                        else:
                            a = demanda[rcl[n]][1] - matrizNueva[rcl[n]][r]
                            if cantPiezas[r] >= a*canPiezas[rcl[n]][r] and a != 0:
                                respuesta.append([])
                                respuesta[indice].append(periodo)
                                respuesta[indice].append(producto[rcl[n]])
                                respuesta[indice].append(tipoPiezas[rcl[n]][r])
                                respuesta[indice].append(a*canPiezas[rcl[n]][r])
                                cantidad[indPieza[r]] = cantidad[indPieza[r]] - a*canPiezas[rcl[n]][r]
                                cantidadPiezas[rcl[n]][r] = cantidadPiezas[rcl[n]][r] - a*canPiezas[rcl[n]][r]
                                matrizNueva[rcl[n]][r] = matrizNueva[rcl[n]][r] + a
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

            with open("Periodos_50_50_10_" + str(iteracion) + "_" + str(itera) + "_" + str(iteraciones+1) + ".txt", "w") as crear:
                #print(productosDemanda, file=crear)
                for k in range(len(respuesta)):
                    print(respuesta[k][0], respuesta[k][1], respuesta[k][2], respuesta[k][3], file=crear)

            with open("InfLE_50_50_10_" + str(iteracion) + "_" + str(itera) + "_" + str(iteraciones+1) + ".txt", "w") as nuevo:
                print(periodos, file=nuevo)
                print(periodo, file=nuevo)
                print(sumar, file=nuevo)
                print(prodTerminados, file=nuevo)
                print(productosMinimos, file=nuevo)
                print(productosDemanda, file=nuevo)
                
                for i in range(len(matrizNueva)):
                    print(min(matrizNueva[i]), i, matrizNueva[i], file=nuevo)

            #print("cantidad")
            #print(cantidad)
            print("Iteracion", iteracion, itera, iteraciones)
            print("productos terminados")
            print(prodTerminados)
            print("piezas en almacen")
            print(sumar)

