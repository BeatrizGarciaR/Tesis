BatchTime <- read.table("BatchTime_50_50_10_10_0_.txt")
PPMMA <- read.table("InfPPMMA_50_50_10_10_0_.txt")
ordenMoldes <- read.table("ordenMoldes_50_50_10_10_0_.txt")
productos <- read.table("Piezas_50_50_10_10_0_.txt")
demanda <- read.table("Demanda_50_50_10_10_0_.txt")
importancia <- read.table("Importancia_50_50_10_10_0_.txt")

periodos <- 48 #periodos cada media hora
producto <- productos[1,1]
pieza <- productos[2,1]
moldes <- productos[3,1]
maquinas <- productos[4,1]
horas <- periodos*productos[5,1]
trabajo <- matrix("", nrow=maquinas, ncol=horas) #10 maquinas, 192 periodos
time <- 1800 #media hora 
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
      while (a+anterior >= time && j < horas){
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

demanda1 <- matrix("", ncol=horas, nrow=producto)
for (i in 1:producto){
  demanda1[i,1] = demanda[i,1] 
  demanda1[i,2] = demanda[i,2]
}


totalPiezas <- data.frame()
for (i in 1:length(PPMMA[,1])){
  for (j in 1:length(BatchTime[,1])){
    if (PPMMA[i,2] == BatchTime[j,1] && PPMMA[i,3] == BatchTime[j,2] && PPMMA[i,4] == BatchTime[j,3]){
      batchporHora <- floor(time/BatchTime[j,4])
      BatchTotales <- floor(PPMMA[i,5]/batchporHora)
      piezasHora <- batchporHora*PPMMA[i,6]
      for (k in 1:BatchTotales){
        totalPiezas <- rbind(totalPiezas, c(PPMMA[i,1], PPMMA[i,2], PPMMA[i,3], PPMMA[i, 4], piezasHora))
      }
    }
  }
}

hechasTipo <- matrix(-2, nrow=maquinas, ncol=horas)
hechasCantidad <- matrix(-2, nrow=maquinas, ncol=horas)
for (m in 1:productos[5,1]){
  for (i in 1:length(trabajo[,1])){ 
    for (j in 1:periodos){
      for (k in 1:length(totalPiezas[,1])){
        if ((i-1) == totalPiezas[k,4] && trabajo[i,j+periodos*(m-1)] == totalPiezas[k,3] && totalPiezas[k,1] == (m-1)){
          hechasTipo[i,j+periodos*(m-1)] = totalPiezas[k,2]
          hechasCantidad[i,j+periodos*(m-1)] = totalPiezas[k,5]
          totalPiezas <- totalPiezas[-k,]
          break
        }
      }
    }
  }
}


tipoPiezas <-  matrix("", nrow=producto, ncol=horas)
cantidadPiezas <- matrix("", nrow=producto, ncol=horas)
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


periodo <- matrix("", ncol=horas)
k <- 1
for (i in 1:length(hechasCantidad[1,])){
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


preferencia <- matrix("", ncol=horas, nrow = length(importancia[,1]))
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
Instancia <- matrix(c(producto, rep("", times=(horas-1))), ncol=horas)
Instancia <- rbind(Instancia, c(horas, rep("", times=(horas-1))))
Instancia <- rbind(Instancia, c(periodos, rep("", times=(horas-1))))
Instancia <- rbind(Instancia, ensamble)
Instancia <- rbind(Instancia, demanda1)
Instancia <- rbind(Instancia, preferencia)
Instancia <- rbind(Instancia, cantidadPiezas)
Instancia <- rbind(Instancia, tipoPiezas)
Instancia <- rbind(Instancia, c("3",rep("",times=(horas-1))))
Instancia <- rbind(Instancia, periodo)
Instancia[length(Instancia[,1]),1] = "-1"


write.table(Instancia,file="Instancia_Prueba_50_50_10_10_0_.txt", sep=" ", col.names=FALSE, row.names=FALSE,quote=FALSE)

