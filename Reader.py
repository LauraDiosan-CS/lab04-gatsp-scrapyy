from math import sqrt


class Reader:
    def euclid(self,x1,x2,y1,y2):
        return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

    def read2(self,fileName):
        f = open(fileName,"r")
        f.readline()
        f.readline()
        f.readline()
        aux = f.readline()
        aux = aux.split(" ")
        n = int(aux[2])
        f.readline()
        f.readline()
        coord = [[0,0] for i in range(n)]
        for i in range(n):
            aux = f.readline()
            aux = aux.split(" ")
            coord[int(aux[0])-1] = [float(aux[1]),float(aux[2])]
        param={}
        param['noNodes'] = n
        mat = []
        for i in range(n):
            aux = []
            for j in range(n):
                aux.append(self.euclid(coord[i][0],coord[j][0],coord[i][1],coord[j][1]))
            mat.append(aux)
        param['mat'] = mat
        return param


    def read(self,fileName):
        f = open(fileName, "r")
        n = int(f.readline())
        param = {}
        mat = []
        param['noNodes'] = n
        for i in range(0, n):
            aux = []
            line = f.readline()
            h = line.split(",")
            for j in h:
                if j!="":
                    aux.append(float(j))
            mat.append(aux)
        param['mat'] = mat
        return param