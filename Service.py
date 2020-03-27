import random

from model.Chromosome import Chromosome
from repository.Repository import Repository


class Service:
    def __init__(self,param):
        self.problParam = param
        self.repo = Repository()

    def selectParents(self,noNodes):
        r = [0,0]
        h = [-1,-1]
        s=-1
        c = -1
        for i in range(2):
            o=random.sample(range(noNodes),1)[0]
            r[i] = self.repo.get(o)
            c = o
            for j in range(20):
                idx = random.sample(range(noNodes),1)[0];
                if self.repo.get(idx).getFitness() < r[i].getFitness() and (s == -1 or s != idx):
                    r[i] = self.repo.get(idx)
                    c = idx
                    h[i] = idx
            s = c
        return [r[0].clone(),r[1].clone()]


    def solve(self, noChrom, noIter, cross, mutation):
        for i in range(0,noChrom):
            self.repo.add(Chromosome(self.problParam))

        self.repo.sort()
        p = Repository()
        #print(self.repo.get(0))
        for i in range(0,noIter):
            repo1 = Repository()
            #repo1.add(self.repo.get(0))
            for j in range(0,noChrom):
                if random.uniform(0,1) <= cross:
                    parents = self.selectParents(noChrom)
                    c = parents[0].crossover(parents[1])
                    if random.uniform(0,1) <= mutation:
                        c.mutation()
                else:
                    c = self.repo.get(j).clone()
                    if random.uniform(0,1) <= mutation:
                        c.mutation()
                repo1.add(c)
            repo1.sort()
            self.repo = repo1
            p.add(self.repo.get(0))
        return p