import random
from random import randint, seed

def generateARandomPermutation(n):
    perm = [i for i in range(1,n)]
    random.shuffle(perm)
    perm.insert(0,0)
    return perm


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = self.calcFitness()

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def clone(self):
        c = Chromosome(self.__problParam)
        l = []
        for i in self.__repres:
            l.append(i)
        c.repres = l
        c.fitness = self.calcFitness()
        return c

    def calcFitness(self):
        s = 0.0
        for i in range(0,self.__problParam['noNodes'] - 1):
            s = s + self.__problParam['mat'][self.repres[i]][self.repres[i+1]]
        s = s + self.__problParam['mat'][0][self.__repres[self.__problParam['noNodes']-1]]
        return s

    def getFitness(self):
        return self.__fitness

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noNodes'] - 2)
        pos2 = randint(-1, self.__problParam['noNodes'] - 2)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        neigh = c.__repres[1:]
        ch = self.__repres[1:]
        newrepres = neigh[pos1: pos2]
        for el in ch[pos2:] + ch[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['noNodes'] - pos1 - 1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        newrepres.insert(0, 0)
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        offspring.__fitness = offspring.calcFitness()

        return offspring

    def mutation(self):
        # insert mutation
        pos1 = randint(1, self.__problParam['noNodes'] - 2)
        pos2 = randint(1, self.__problParam['noNodes'] - 2)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        self.__fitness = self.calcFitness()

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness