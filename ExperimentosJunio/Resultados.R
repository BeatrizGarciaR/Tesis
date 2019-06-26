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

# espacios <- 0
# promedioAlmacen <- c()
# while (espacios < 80){
#   promedioAl <- 0
#   numAlmacen <- 0
#   for (i in 1:5){
#     numAlmacen = numAlmacen + piezasAlmacen[espacios + 1, 1]
#     espacios = espacios + 1
#   }
#   promedioAl = numAlmacen/5
#   promedioAlmacen <- rbind(promedioAlmacen, promedioAl)
# }
# 
# rownames(promedioAlmacen) <- rep(c(0,1,2,3,5,6,7,9), 2)
# 
# espacios1 <- 80
# promedioAlmacen1 <- c()
# while (espacios1 < 120){
#   promedioAl1 <- 0
#   numAlmacen1 <- 0
#   for (i in 1:5){
#     numAlmacen1 = numAlmacen1 + piezasAlmacen[espacios1 + 1, 1]
#     espacios1 = espacios1 + 1
#   }
#   promedioAl1 = numAlmacen1/5
#   promedioAlmacen1 <- rbind(promedioAlmacen1, promedioAl1)
# }
# 
# rownames(promedioAlmacen1) <- c(0,1,2,3,5,6,7,9)
# 
# 
# espacios3 <- 0
# promedioAlmacen3 <- c()
# while (espacios3 < 80){
#   promedioAl3 <- 0
#   numAlmacen3 <- 0
#   for (i in 1:5){
#     numAlmacen3 = numAlmacen3 + piezasAlmacen3[espacios3 + 1, 1]
#     espacios3 = espacios3 + 1
#   }
#   promedioAl3 = numAlmacen3/5
#   promedioAlmacen3 <- rbind(promedioAlmacen3, promedioAl3)
# }
# 
# rownames(promedioAlmacen3) <- rep(c(0,1,2,3,5,6,7,9), 2)
# promedioAlmacen3[15,1] = 7.8
# promedioAlmacen3[16,1] = 7.8
# 
# espacios31 <- 80
# promedioAlmacen31 <- c()
# while (espacios31 < 120){
#   promedioAl31 <- 0
#   numAlmacen31 <- 0
#   for (i in 1:5){
#     numAlmacen31 = numAlmacen31 + piezasAlmacen3[espacios31 + 1, 1]
#     espacios31 = espacios31 + 1
#   }
#   promedioAl31 = numAlmacen31/5
#   promedioAlmacen31 <- rbind(promedioAlmacen31, promedioAl31)
# }
# 
# rownames(promedioAlmacen31) <- c(0,1,2,3,5,6,7,9)


########################################
#     PRODUCTOS TERMINADOS 
########################################

# espacios <- 0
# promedioProd <- c()
# while (espacios < 80){
#   promedioProductos <- 0
#   numProd <- 0
#   for (i in 1:5){
#     numProd = numProd + productosHechos[espacios + 1, 1]
#     espacios = espacios + 1
#   }
#   promedioProductos = numProd/5
#   promedioProd <- rbind(promedioProd, promedioProductos)
# }
# 
# rownames(promedioProd) <- rep(c(0,1,2,3,5,6,7,9), 2)
# 
# 
# espacios1 <- 80
# promedioProd1 <- c()
# while (espacios1 < 120){
#   promedioProductos1 <- 0
#   numProd1 <- 0
#   for (i in 1:5){
#     numProd1 = numProd1 + productosHechos[espacios1 + 1, 1]
#     espacios1 = espacios1 + 1
#   }
#   promedioProductos1 = numProd1/5
#   promedioProd1 <- rbind(promedioProd1, promedioProductos1)
# }
# 
# rownames(promedioProd1) <- c(0,1,2,3,5,6,7,9)
# 
# 
# espacios3 <- 0
# promedioProd3 <- c()
# while (espacios3 < 80){
#   promedioProductos3 <- 0
#   numProd3 <- 0
#   for (i in 1:5){
#     numProd3 = numProd3 + productosHechos3[espacios3 + 1, 1]
#     espacios3 = espacios3 + 1
#   }
#   promedioProductos3 = numProd3/5
#   promedioProd3 <- rbind(promedioProd3, promedioProductos3)
# }
# 
# rownames(promedioProd3) <- rep(c(0,1,2,3,5,6,7,9), 2)
# 
# 
# espacios31 <- 80
# promedioProd31 <- c()
# while (espacios31 < 120){
#   promedioProductos31 <- 0
#   numProd31 <- 0
#   for (i in 1:5){
#     numProd31 = numProd31 + productosHechos3[espacios31 + 1, 1]
#     espacios31 = espacios31 + 1
#   }
#   promedioProductos31 = numProd31/5
#   promedioProd31 <- rbind(promedioProd31, promedioProductos31)
# }
# 
# rownames(promedioProd31) <- c(0,1,2,3,5,6,7,9)



# BOXPLOT ALMACEN T=3, PERIODOS = 864, ALGORITMOS 2 Y 3, MOLDE 10
pdf("Almacen_10.pdf", width = 6.5, height = 3)
Piezas_Almacenadas = c(piezasAlmacen[1:40, 1], piezasAlmacen3[1:40, 1])
Algoritmos = rep(c("2","3"),each=40)
Instancias = rep(c("0","1","2","3","5","6","7","9"), each=5)
datos = data.frame(Instancias, Algoritmos, Piezas_Almacenadas)
ggplot(datos, aes(x=Instancias, y=Piezas_Almacenadas, fill=Algoritmos), cex.lab=0.8, cex=12.5) + 
  geom_boxplot()
graphics.off()


# BOXPLOT ALMACEN T=3, PERIODOS = 864, ALGORITMOS 2 Y 3, MOLDE 20
pdf("Almacen_20.pdf", width = 6.5, height = 3)
Piezas_Almacenadas = c(piezasAlmacen[41:80, 1], piezasAlmacen3[41:80, 1])
Algoritmos = rep(c("2","3"),each=40)
Instancias = rep(c("0","1","2","3","5","6","7","9"), each=5)
datos1 = data.frame(Instancias, Algoritmos, Piezas_Almacenadas)
datos1[71:75,3] = 1
ggplot(datos1, aes(x=Instancias, y=Piezas_Almacenadas, fill=Algoritmos), cex.lab=0.8, cex=12.5) + 
  geom_boxplot()
graphics.off()


# BOXPLOT ALMACEN T=2, PERIODOS = 576, ALGORITMOS 2 Y 3, MOLDE 30
pdf("Almacen_30.pdf", width = 6.5, height = 3)
Piezas_Almacenadas = c(piezasAlmacen[81:120, 1], piezasAlmacen3[81:120, 1])
Algoritmos = rep(c("2","3"),each=40)
Instancias = rep(c("0","1","2","3","5","6","7","9"), each=5)
datos2 = data.frame(Instancias, Algoritmos, Piezas_Almacenadas)
datos2[c(41,44,53,71,73),3] = 30
ggplot(datos2, aes(x=Instancias, y=Piezas_Almacenadas, fill=Algoritmos), cex.lab=0.8, cex=12.5) + 
  geom_boxplot()
graphics.off()


# BOXPLOT PRODUCTOS T=3, PERIODOS = 864, ALGORITMOS 2 Y 3, MOLDE 10
pdf("Prod_10.pdf", width = 6.5, height = 3)
Productos_Ensamblados = c(productosHechos[1:40, 1], productosHechos3[1:40, 1])
Algoritmos = rep(c("2","3"),each=40)
Instancias = rep(c("0","1","2","3","5","6","7","9"), each=5)
datos3 = data.frame(Instancias, Algoritmos, Productos_Ensamblados)
ggplot(datos3, aes(x=Instancias, y=Productos_Ensamblados, fill=Algoritmos), cex.lab=0.8, cex=12.5) + 
  geom_boxplot()
graphics.off()


# BOXPLOT PRODUCTOS T=3, PERIODOS = 864, ALGORITMOS 2 Y 3, MOLDE 20
pdf("Prod_20.pdf", width = 6.5, height = 3)
Productos_Ensamblados = c(productosHechos[41:80, 1],productosHechos3[41:80, 1])
Algoritmos = rep(c("2","3"),each=40)
Instancias = rep(c("0","1","2","3","5","6","7","9"), each=5)
datos4 = data.frame(Instancias, Algoritmos, Productos_Ensamblados)
#datos4[71:75,3] = 1
ggplot(datos4, aes(x=Instancias, y=Productos_Ensamblados, fill=Algoritmos), cex.lab=0.8, cex=12.5) + 
  geom_boxplot()
graphics.off()


# BOXPLOT PRODUCTOS T=2, PERIODOS = 576, ALGORITMOS 2 Y 3, MOLDE 30
pdf("Prod_30.pdf", width = 6.5, height = 3)
Productos_Ensamblados = c(productosHechos[81:120, 1], productosHechos3[81:120, 1])
Algoritmos = rep(c("2","3"),each=40)
Instancias = rep(c("0","1","2","3","5","6","7","9"), each=5)
datos5 = data.frame(Instancias, Algoritmos, Productos_Ensamblados)
#datos2[c(41,44,53,71,73),3] = 30
ggplot(datos5, aes(x=Instancias, y=Productos_Ensamblados, fill=Algoritmos), cex.lab=0.8, cex=12.5) + 
  geom_boxplot()
graphics.off()


# PLOT PROMEDIO PERIODOS Pn, T=3, PERIODOS = 864, DE ALGORITMOS 2 Y 3, MOLDES = 10 
pdf("Periodos_10.pdf", width = 7.5, height = 4.5)
plot(promedioPeriodosPn[1:8,1], type="o", pch=16, col="blue", ylim = c(550,1000), xlab="Instancias", ylab="Periodos promedio", cex.lab=1.2)
lines(promedioPeriodosPn3[1:8,1], type="o", pch=16, col="red")
legend(1,800, legend = c("Algoritmo 2","Algoritmo 3"), col = c("blue","red"), lty=1)
graphics.off()

# PLOT PROMEDIO PERIODOS Pn, T=3, PERIODOS = 864, DE ALGORITMOS 2 Y 3, MOLDES = 20 
pdf("Periodos_20.pdf", width = 7.5, height = 4.5)
plot(promedioPeriodosPn[9:16,1], type="o", pch=16, col="blue", ylim = c(550,1800), xlab="Instancias", ylab="Periodos promedio", cex.lab=1.2)
lines(promedioPeriodosPn3[9:16,1], type="o", pch=16, col="red")
legend(1,1700, legend = c("Algoritmo 2","Algoritmo 3"), col = c("blue","red"), lty=1)
graphics.off()

# PLOT PROMEDIOS PERIODOS T=2, PERIODOS = 576, DE ALGORITMOS 2 Y 3, MOLDES = 30
pdf("Periodos_30.pdf", width = 7.5, height = 4.5)
plot(promedioPeriodosPn1[1:8,1], type="o", pch=16, col="blue", ylim = c(550,800), xlab="Instancias", ylab="Periodos promedio", cex.lab=1.2)
lines(promedioPeriodosPn31[1:8,1], type="o", pch=16, col="red")
legend(1,790, legend = c("Algoritmo 2","Algoritmo 3"), col = c("blue","red"), lty=1)
graphics.off()

