class ProductoEnsamble:

    def __init__(self):
        self.n = 6*15
        self.npa = 12
        self.npb = 17
        self.npc = 14
        self.npd = 15
        self.npab = self.npa*2
        self.npap = self.npa*2
        self.npaca = self.npa
        self.npac = self.npa
        self.npbb = self.npb*2
        self.npbp = self.npb*2
        self.npbca = self.npb
        self.npbc = self.npb
        self.npcb = self.npc*2
        self.npcp = self.npc*2
        self.npcca = self.npc
        self.npcc = self.npc
        self.npdb = self.npd*2
        self.npdp = self.npd*2
        self.npdca = self.npd 
        self.npdc = self.npd
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.p5 = 0
        self.p6 = 0
        self.p8 = 0
        self.p9 = 0
        self.p10 = 0
        self.p11 = 0
        self.time1 = [0,1,2,3,4,5,36,37,38,39,40,41]
        self.time2 = [0,1,2,3,4,5]
        self.time3 = [20,23,26,29,32,35,38,41,44,47,50,53]
        self.time4 = [9,13,17]
        self.time5 = [18,19,20,21,22,23]
        self.time6 = [6,7,8,9,10,11,48,49,50,51,52,53]
        self.time8 = [23,29,35]
        self.time9 = [24,25,26,27,28,29]
        self.time10 = [43,45,47]
        self.time11 = [43,45,47]
        self.demanda = [self.npb,self.npd,self.npc,self.npa]
        self.piezasa = [self.p1,self.p6,self.p11,self.p3,self.p1,self.p6,self.p9,self.p4,self.p5,self.p2,self.p9,self.p3,self.p5,self.p2,self.p10,self.p8]
        self.cantidadpieza = [self.npbb,self.npbp,self.npbca,self.npbc,self.npdb,self.npdp,self.npdca,self.npdc,self.npcb,self.npcp,self.npcca,self.npcc,self.npab,self.npap,self.npaca,self.npac]
        self.ep1 = 5
        self.ep2 = 3
        self.ep5 = 5
        self.ep6 = 3
        self.ep9 = 2
        self.ep10 = 2
        self.ep11 = 2

    def piezas(self, time):
        for t1 in range(len(self.time1)):
            if time == self.time1[t1]:
                self.p1 = self.p1 + 6
        for t2 in range(len(self.time2)):
            if time == self.time2[t2]:
                self.p2 = self.p2 + 10
        for t3 in range(len(self.time3)):
            if time == self.time3[t3]:
                self.p3 = self.p3 + 3
        for t4 in range(len(self.time4)):
            if time == self.time4[t4]:
                self.p4 = self.p4 + 5
        for t5 in range(len(self.time5)):
            if time == self.time5[t5]:
                self.p5 = self.p5 + 10
        for t6 in range(len(self.time6)):
            if time == self.time6[t6]:
                self.p6 = self.p6 + 6
        for t8 in range(len(self.time8)):
            if time == self.time8[t8]:
                self.p8 = self.p8 + 5
        for t9 in range(len(self.time9)):
            if time == self.time9[t9]:
                self.p9 = self.p9 + 8
        for t10 in range(len(self.time10)):
            if time == self.time10[t10]:
                self.p10 = self.p10 + 5
        for t11 in range(len(self.time11)):
            if time == self.time11[t11]:
                self.p11 = self.p11 + 6
        return(self.p1,self.p6,self.p11,self.p3,self.p1,self.p6,self.p9,self.p4,self.p5,self.p2,self.p9,self.p3,self.p5,self.p2,self.p10,self.p8)

    def matrizPieza(self,a):
        matriz = []
        for i in range(4):
            matriz.append([])
            for j in range(4):
                matriz[i].append(a[4*i+j])
        return(matriz)
    
    def piezaRequerida(self):
        matriz = []
        for i in range(4):
            matriz.append([])
            for j in range(4):
                matriz[i].append(self.cantidadpieza[4*i+j])
        return(matriz)
       

    def piezaP(self):
        matriz = []
        for i in range(4):
            matriz.append([])
            for j in range(4):
                matriz[i].append(0)
        return(matriz)
        
        
P = ProductoEnsamble()
pa = 4 
pb = 1
pc = 3
pd = 2
time = 0
producto = [pb,pd,pc,pa]
piezasRequeridas = P.piezaRequerida()
piezasProducidas = P.piezaP()
while producto[0] is not 0 and producto[1] is not 0 and producto[2] is not 0 and producto[3] is not 0:
    for n in range(len(producto)):
        if producto[n] is not 0:
            if piezasRequeridas[n][0:4] <= piezasProducidas[n][0:4]:
                brazos = 0
                piernas = 0
                cabezas = 0
                cuerpos = 0
                piezasEnsambladas = []
                while piezasRequeridas[n][0] > 0:
                    brazos = brazos + 5
                    piezasRequeridas[n][0] = piezasRequeridas[n][0] - 5
                    a = P.piezas(time)
                    piezasProducidas = P.matrizPieza(a)
                    time = time + 1
                piezasEnsambladas.append(brazos)
                for i in range(4):
                    if piezasProducidas[n][0] == piezasProducidas[i][0]:
                        piezasProducidas[i][0] = piezasProducidas[i][0] - brazos
                while piezasRequeridas[n][1] > 0:
                    piernas = piernas + 3
                    piezasRequeridas[n][1] = piezasRequeridas[n][1] - 3
                    a = P.piezas(time)
                    piezasProducidas = P.matrizPieza(a)
                    time = time + 1
                piezasEnsambladas.append(piernas)
                for i in range(4):
                    if piezasProducidas[n][1] == piezasProducidas[i][1]:
                        piezasProducidas[i][1] = piezasProducidas[i][1] - piernas
                while piezasRequeridas[n][2] > 0:
                    cabezas = cabezas + 2
                    cuerpos = cuerpos + 2
                    piezasRequeridas[n][2] = piezasRequeridas[n][2] - 2
                    piezasRequeridas[n][3] = piezasRequeridas[n][3] - 2
                    a = P.piezas(time)
                    piezasProducidas = P.matrizPieza(a)
                    time = time + 1
                piezasEnsambladas.append(cabezas) 
                piezasEnsambladas.append(cuerpos)
                for i in range(4):
                    if piezasProducidas[n][2] == piezasProducidas[i][2]:
                        piezasProducidas[i][2] = piezasProducidas[i][2] - cuerpos
                for i in range(4):
                    if piezasProducidas[n][3] == piezasProducidas[i][3]:
                        piezasProducidas[i][3] = piezasProducidas[i][3] - cabezas
                print(piezasEnsambladas)
                print(producto[n])
                producto[n] = 0
            else:
                a = P.piezas(time)
                piezasProducidas = P.matrizPieza(a)
                time = time + 1
                    
                    
                    