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
      
      periodosPn <- rbind(periodosPn, informacionPeriodosLE[length(informacionPeriodosLE[,1]),1])
      
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
      informacionPeriodosLE3 <- read.table(paste("Periodos3_50_50_10_",itera,"_",iter, "_", iteraciones,".txt", sep = ""), header = TRUE, fill = TRUE, sep = "\t")
      
      #periodostotalesPPMM3 <- rbind(periodostotalesPPMM3, as.numeric(as.character(informacionLE3[1,1])))
      
      periodosPn3 <- rbind(periodosPn3, informacionPeriodosLE3[length(informacionPeriodosLE3[,1]),1])
      
      piezasAlmacen3 <- rbind(piezasAlmacen3, as.numeric(as.character(informacionLE3[2,1])))
      
      productosHechos3 <- rbind(productosHechos3, as.numeric(as.character(informacionLE3[3,1])))
    }
  }
}


#informacionPeriodosLE3 <- read.table("InfLE_50_50_10_10_0_1_copia.txt")
#a <- as.numeric(as.character(informacionPeriodosLE3[1,1]))
