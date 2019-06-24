library(ggplot2)

numMaquina = c(10,20,30)
numIns = c(0,1,2,3,5,6,7,9)

periodostotalesPPMM <- c()
periodosPn <- c()
piezasAlmacen <- c()
productosHechos <- c()


for (itera in numMaquina){
  for (iter in numIns){
    for (iteraciones in 1:5){
      
      print(paste(itera,iter,iteraciones))
      
      informacionLE <- read.table(paste("InfLE_50_50_10_",itera,"_",iter, "_", iteraciones,".txt", sep = ""), header = TRUE, fill = TRUE, sep = "\t")
      informacionPeriodosLE <- read.table(paste("Periodos_50_50_10_",itera,"_",iter, "_", iteraciones,".txt", sep = ""), header = TRUE, fill = TRUE)
      
      #periodostotalesPPMM <- rbind(periodostotalesPPMM, as.numeric(as.character(informacionLE[1,1])))
      
      periodosPn <- rbind(periodosPn, as.numeric(informacionPeriodosLE[length(informacionPeriodosLE[,1]),1]))
      
      piezasAlmacen <- rbind(piezasAlmacen, as.numeric(as.character(informacionLE[2,1])))
      
      productosHechos <- rbind(productosHechos, as.numeric(as.character(informacionLE[3,1])))
    }
  }
}

periodostotalesPPMM3 <- c()
periodosPn3 <- c()
piezasAlmacen3<- c()
productosHechos3 <- c()


for (itera in numMaquina){
  for (iter in numIns){
    for (iteraciones in 1:5){
      
      print(paste("hola", itera,iter,iteraciones))
      
      informacionLE3 <- read.table(paste("InfLE3_50_50_10_",itera,"_",iter, "_", iteraciones,".txt", sep = ""), header = TRUE, fill = TRUE, sep = "\t")
      informacionPeriodosLE3 <- read.table(paste("Periodos3_50_50_10_",itera,"_",iter, "_", iteraciones,".txt", sep = ""), header = TRUE, fill = TRUE)
      
      #periodostotalesPPMM3 <- rbind(periodostotalesPPMM3, as.numeric(as.character(informacionLE3[1,1])))
      
      periodosPn3 <- rbind(periodosPn3, informacionPeriodosLE3[length(informacionPeriodosLE3[,1]),1])
      
      piezasAlmacen3 <- rbind(piezasAlmacen3, as.numeric(as.character(informacionLE3[2,1])))
      
      productosHechos3 <- rbind(productosHechos3, as.numeric(as.character(informacionLE3[3,1])))
    }
  }
}


########################################
#   PROMEDIO PERIODOS PN
########################################

espacios <- 0
promedioPeriodosPn <- c()
while (espacios < 80){
  promedioPeriodo <- 0
  numPeriodos <- 0
  for (i in 1:5){
    numPeriodos = numPeriodos + periodosPn[espacios + 1, 1]
    espacios = espacios + 1
  }
  promedioPeriodo = numPeriodos/5
  promedioPeriodosPn <- rbind(promedioPeriodosPn, promedioPeriodo)
}

rownames(promedioPeriodosPn) <- rep(c(0,1,2,3,5,6,7,9), 2)


espacios1 <- 80
promedioPeriodosPn1 <- c()
while (espacios1 < 120){
  promedioPeriodo1 <- 0
  numPeriodos1 <- 0
  for (i in 1:5){
    numPeriodos1 = numPeriodos1 + periodosPn[espacios1 + 1, 1]
    espacios1 = espacios1 + 1
  }
  promedioPeriodo1 = numPeriodos1/5
  promedioPeriodosPn1 <- rbind(promedioPeriodosPn1, promedioPeriodo1)
}

rownames(promedioPeriodosPn1) <-c(0,1,2,3,5,6,7,9)


espacios3 <- 0
promedioPeriodosPn3 <- c()
while (espacios3 < 80){
  promedioPeriodo3 <- 0
  numPeriodos3 <- 0
  for (i in 1:5){
    numPeriodos3 = numPeriodos3 + periodosPn3[espacios3 + 1, 1]
    espacios3 = espacios3 + 1
  }
  promedioPeriodo3 = numPeriodos3/5
  promedioPeriodosPn3 <- rbind(promedioPeriodosPn3, promedioPeriodo3)
}

rownames(promedioPeriodosPn3) <- rep(c(0,1,2,3,5,6,7,9), 2)


espacios31 <- 80
promedioPeriodosPn31 <- c()
while (espacios31 < 120){
  promedioPeriodo31 <- 0
  numPeriodos31 <- 0
  for (i in 1:5){
    numPeriodos31 = numPeriodos31 + periodosPn3[espacios31 + 1, 1]
    espacios31 = espacios31 + 1
  }
  promedioPeriodo31 = numPeriodos31/5
  promedioPeriodosPn31 <- rbind(promedioPeriodosPn31, promedioPeriodo31)
}

rownames(promedioPeriodosPn31) <- c(0,1,2,3,5,6,7,9)


########################################
#     PIEZAS ALMACENADAS 
########################################

espacios <- 0
promedioAlmacen <- c()
while (espacios < 80){
  promedioAl <- 0
  numAlmacen <- 0
  for (i in 1:5){
    numAlmacen = numAlmacen + piezasAlmacen[espacios + 1, 1]
    espacios = espacios + 1
  }
  promedioAl = numAlmacen/5
  promedioAlmacen <- rbind(promedioAlmacen, promedioAl)
}

rownames(promedioAlmacen) <- rep(c(0,1,2,3,5,6,7,9), 2)

espacios1 <- 80
promedioAlmacen1 <- c()
while (espacios1 < 120){
  promedioAl1 <- 0
  numAlmacen1 <- 0
  for (i in 1:5){
    numAlmacen1 = numAlmacen1 + piezasAlmacen[espacios1 + 1, 1]
    espacios1 = espacios1 + 1
  }
  promedioAl1 = numAlmacen1/5
  promedioAlmacen1 <- rbind(promedioAlmacen1, promedioAl1)
}

rownames(promedioAlmacen1) <- c(0,1,2,3,5,6,7,9)


espacios3 <- 0
promedioAlmacen3 <- c()
while (espacios3 < 80){
  promedioAl3 <- 0
  numAlmacen3 <- 0
  for (i in 1:5){
    numAlmacen3 = numAlmacen3 + piezasAlmacen3[espacios3 + 1, 1]
    espacios3 = espacios3 + 1
  }
  promedioAl3 = numAlmacen3/5
  promedioAlmacen3 <- rbind(promedioAlmacen3, promedioAl3)
}

rownames(promedioAlmacen3) <- rep(c(0,1,2,3,5,6,7,9), 2)
promedioAlmacen3[15,1] = 7.8
promedioAlmacen3[16,1] = 7.8

espacios31 <- 80
promedioAlmacen31 <- c()
while (espacios31 < 120){
  promedioAl31 <- 0
  numAlmacen31 <- 0
  for (i in 1:5){
    numAlmacen31 = numAlmacen31 + piezasAlmacen3[espacios31 + 1, 1]
    espacios31 = espacios31 + 1
  }
  promedioAl31 = numAlmacen31/5
  promedioAlmacen31 <- rbind(promedioAlmacen31, promedioAl31)
}

rownames(promedioAlmacen31) <- c(0,1,2,3,5,6,7,9)


########################################
#     PRODUCTOS TERMINADOS 
########################################

espacios <- 0
promedioProd <- c()
while (espacios < 80){
  promedioProductos <- 0
  numProd <- 0
  for (i in 1:5){
    numProd = numProd + productosHechos[espacios + 1, 1]
    espacios = espacios + 1
  }
  promedioProductos = numProd/5
  promedioProd <- rbind(promedioProd, promedioProductos)
}

rownames(promedioProd) <- rep(c(0,1,2,3,5,6,7,9), 2)


espacios1 <- 80
promedioProd1 <- c()
while (espacios1 < 120){
  promedioProductos1 <- 0
  numProd1 <- 0
  for (i in 1:5){
    numProd1 = numProd1 + productosHechos[espacios1 + 1, 1]
    espacios1 = espacios1 + 1
  }
  promedioProductos1 = numProd1/5
  promedioProd1 <- rbind(promedioProd1, promedioProductos1)
}

rownames(promedioProd1) <- c(0,1,2,3,5,6,7,9)


espacios3 <- 0
promedioProd3 <- c()
while (espacios3 < 80){
  promedioProductos3 <- 0
  numProd3 <- 0
  for (i in 1:5){
    numProd3 = numProd3 + productosHechos3[espacios3 + 1, 1]
    espacios3 = espacios3 + 1
  }
  promedioProductos3 = numProd3/5
  promedioProd3 <- rbind(promedioProd3, promedioProductos3)
}

rownames(promedioProd3) <- rep(c(0,1,2,3,5,6,7,9), 2)


espacios31 <- 80
promedioProd31 <- c()
while (espacios31 < 120){
  promedioProductos31 <- 0
  numProd31 <- 0
  for (i in 1:5){
    numProd31 = numProd31 + productosHechos3[espacios31 + 1, 1]
    espacios31 = espacios31 + 1
  }
  promedioProductos31 = numProd31/5
  promedioProd31 <- rbind(promedioProd31, promedioProductos31)
}

rownames(promedioProd31) <- c(0,1,2,3,5,6,7,9)




# BOXPLOT ALMACEN T=3, PERIODOS = 864, DE ALGORITMOS 2 Y 3, MOLDES = 10 Y 20
png("Almacen_3_10Y20.png", width=300, height=300)
variety=c("0","1","2","3","5","6","7","9","0","1","2","3","5","6","7","9")
treatment=rep(c("2","3"),each=16)
note=rbind(promedioAlmacen, promedioAlmacen3)
data = data.frame(variety, treatment, note)
ggplot(data, aes(x=variety, y=note, fill=treatment)) + 
  geom_boxplot()

graphics.off()



# BOXPLOT PRODUCTOS ENSAMBLADOS, T=3, PERIODOS = 864, DE ALGORITMOS 2 Y 3, MOLDES = 10 Y 20
png("Productos_3_10Y20.png", width=300, height=300)
variety1=c("0","1","2","3","5","6","7","9","0","1","2","3","5","6","7","9")
treatment1=rep(c("2","3"),each=16)
note1=rbind(promedioProd, promedioProd3)
data1 = data.frame(variety1, treatment1, note1)
ggplot(data1, aes(x=variety1, y=note1, fill=treatment1)) + 
  geom_boxplot()
graphics.off()


# PLOT PROMEDIO PERIODOS Pn, T=3, PERIODOS = 864, DE ALGORITMOS 2 Y 3, MOLDES = 10 Y 20
png("Periodos_3_10Y20.png", width=300, height=300)
plot(promedioPeriodosPn[1:16,1], type="o", pch=16, col="blue")
lines(promedioPeriodosPn3[1:16,1], type="o", pch=16, col="red")
graphics.off()


# PLOT ALMACEN T=2, PERIODOS = 576, DE ALGORITMOS 2 Y 3, MOLDES = 30
png("Almacen_2_30.png", width=300, height=300)
variety2=c("0","1","2","3","5","6","7","9")
treatment2=rep(c("2","3"),each=8)
note2=rbind(promedioAlmacen1, promedioAlmacen31)
aux1 = data.frame(variety2, treatment2, note2)
ggplot(aux1, aes(fill=treatment2, x=variety2, y=note2)) + 
  geom_bar(position="dodge", stat="identity")
graphics.off()


# PLOT PRODUCTOS ENSAMBLADOS T=2, PERIODOS = 576, DE ALGORITMOS 2 Y 3, MOLDES = 30
png("Productos_2_30.png", width=300, height=300)
variety3=c("0","1","2","3","5","6","7","9")
treatment3=rep(c("2","3"),each=8)
note3=rbind(promedioProd1, promedioProd31)
aux2 = data.frame(variety3, treatment3, note3)
ggplot(aux2, aes(fill=treatment3, x=variety3, y=note3)) + 
  geom_bar(position="dodge", stat="identity")
graphics.off()


# PLOT PROMEDIOS PERIODOS T=2, PERIODOS = 576, DE ALGORITMOS 2 Y 3, MOLDES = 30
png("Periodos_2_30.png", width=300, height=300)
plot(promedioPeriodosPn31[1:8,1], type="o", pch=16, col="blue")
lines(promedioPeriodosPn1[1:8,1], type="o", pch=16, col="red")
graphics.off()

