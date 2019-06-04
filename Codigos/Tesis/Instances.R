BatchTime <- read.table("BatchTime_50_50_10_10_0_.txt")
PPMMA <- read.table("InfPPMMA_50_50_10_10_0_.txt")
ordenMoldes <- read.table("ordenMoldes_50_50_10_10_0_.txt")
productos <- read.table("Piezas_50_50_10_10_0_.txt")
demanda <- read.table("Demanda_50_50_10_10_0_.txt")
importancia <- read.table("Importancia_50_50_10_10_0_.txt")


producto <- productos[1,1]
pieza <- productos[2,1]
moldes <- productos[3,1]
maquinas <- productos[4,1]
periodos <- 72 #periodos (20 min) para las 24 horas del d?a 
periodoTiempo <- periodos*productos[5,1]
time <- 1200 #un minuto tiene 60 segundos (por 20 min)


trabajo <- matrix("", nrow=maquinas, ncol=periodoTiempo) #10 maquinas, 192 periodos
anterior <- 0 
i <- 0
for (m in 1:productos[5,1]){
  maq <- 0
  print(m)
  while (ordenMoldes[i+1,1] != -3){
    j <- periodos*(m-1)
    print(j)
    while (ordenMoldes[i+1,1] != -2){
      a <- ordenMoldes[i+1,2]
      while (a+anterior >= time && j < periodoTiempo){
        trabajo[maq+1,j+1] = ordenMoldes[i+1,1]
        ordenMoldes[i+1,2] = ordenMoldes[i+1,2] - time
        a <- ordenMoldes[i+1,2]
        j = j + 1
      }
      anterior = ordenMoldes[i+1,2]
      i = i + 1
    }
    i = i + 1
    maq = maq + 1
  }
  i = i + 1
}

demanda1 <- matrix("", ncol=periodoTiempo, nrow=producto)
for (i in 1:producto){
  demanda1[i,1] = demanda[i,1] 
  demanda1[i,2] = demanda[i,2]
}


totalPiezas <- data.frame()
for (i in 1:length(BatchTime[,1])){ #Fijo batchTime
  for (j in 1:length(PPMMA[,1])){ #Iterando PPMMA
    if (BatchTime[i,1] == PPMMA[j,2] && BatchTime[i,2] == PPMMA[j,3] && BatchTime[i,3] == PPMMA[j,4]){
      tiempoBatch <- ceiling(BatchTime[i,4]/time)
      if (tiempoBatch == 1){
        BatchTot <- floor(time/BatchTime[i,4])
        piezasPeriodo <- BatchTot*PPMMA[j,6]
        BatchTotales <- ceiling(PPMMA[j,5]/BatchTot)
      }
      else{
        piezasPeriodo <- PPMMA[j,6]
        BatchTotales <- PPMMA[j,5]
      }
      for (k in 1:BatchTotales){
        totalPiezas <- rbind(totalPiezas, c(PPMMA[j,1], PPMMA[j,2], PPMMA[j,3], PPMMA[j, 4], tiempoBatch, piezasPeriodo))
      }
    }
  }
}


totalPiezas1 <- totalPiezas
hechasTipo <- matrix(-2, nrow=maquinas, ncol=periodoTiempo)
hechasCantidad <- matrix(-2, nrow=maquinas, ncol=periodoTiempo)
for (i in 1:length(trabajo[,1])){
  print(paste("primer for", i))
  for (m in 1:productos[5,1]){
    print(paste("segundo for", m))
    aux <- which(totalPiezas1[,1] == (m-1) & totalPiezas1[,4] == (i-1))
    aux1 <- c()
    if (length(aux) > 0){
      j = 1
      while (j <= periodos){
        b <- sample(aux,1)
        while (trabajo[i,j+periodos*(m-1)] == -1){
          j = j + 1
        }
        if (totalPiezas1[b,5] > 1){
          j = j + (totalPiezas1[b,5]-1)
        }
        if (j > periodos){
           break
        }
        if (totalPiezas1[b,3] == trabajo[i,j+periodos*(m-1)]){
          hechasTipo[i,j+periodos*(m-1)] = totalPiezas1[b,2]
          hechasCantidad[i,j+periodos*(m-1)] = totalPiezas1[b,6]
          aux1 <- c(aux1, b)
          aux <- aux[-b]
          j = j + 1
        }
        else{
          j = j + 1
        }
        if (length(aux) == 0){
          break
        }
      }
    }
    if (length(aux1) > 0){
      aux1 <- sort(aux1, decreasing = TRUE)
      for (r in 1:length(aux1)){
        totalPiezas1 <- totalPiezas1[-aux1[r],]
      }
    }
  }
}


tipoPiezas <-  matrix("", nrow=producto, ncol=periodoTiempo)
cantidadPiezas <- matrix("", nrow=producto, ncol=periodoTiempo)
for (i in 1:producto){
  k <- 1
  for (j in 6:length(productos[,1])){
    if (i-1 == productos[j,1]){
      tipoPiezas[i,k] = productos[j,2]
      cantidadPiezas[i,k] = productos[j,3]
      k = k + 1
    }
  }
}


periodo <- matrix("", ncol=periodoTiempo)
k <- 1
for (i in 1:length(hechasCantidad[1,])){
  print(i)
  for (j in 1:length(hechasCantidad[,1])){
    if (hechasCantidad[j,i] != -2){
      periodo <- rbind(periodo, c(""))
      periodo[k,1] = i
      periodo[k,2] = hechasTipo[j,i]
      periodo[k,3] = hechasCantidad[j,i]
      for (r in 4:length(hechasCantidad[1,])){
        periodo[k,r] = ""
      }
      k = k + 1
    }
  }
}


preferencia <- matrix("", ncol=periodoTiempo, nrow = length(importancia[,1]))
imp <- sort(importancia[,2])
ir <- 1
for (i in 1:length(importancia[,1])){
  a <- which(importancia[,2] == imp[ir])
  for (j in 1:length(a)){
    preferencia[ir+j-1,1] = importancia[a[j],1]
    preferencia[ir+j-1,2] = importancia[a[j],2]
  }
  ir = ir + length(a)
  if (ir > 50){
    break
  }
}



ensamble <- c("100","150","100","150")
Instancia <- matrix(c(producto, rep("", times=(periodoTiempo-1))), ncol=periodoTiempo)
Instancia <- rbind(Instancia, c(periodoTiempo, rep("", times=(periodoTiempo-1))))
Instancia <- rbind(Instancia, c(periodos, rep("", times=(periodoTiempo-1))))
Instancia <- rbind(Instancia, ensamble)
Instancia <- rbind(Instancia, demanda1)
Instancia <- rbind(Instancia, preferencia)
Instancia <- rbind(Instancia, cantidadPiezas)
Instancia <- rbind(Instancia, tipoPiezas)
Instancia <- rbind(Instancia, c("3",rep("",times=(periodoTiempo-1))))
Instancia <- rbind(Instancia, periodo)
Instancia[length(Instancia[,1]),1] = "-1"


write.table(Instancia,file="Instancia_Prueba_50_50_10_10_0_.txt", sep=" ", col.names=FALSE, row.names=FALSE,quote=FALSE)

