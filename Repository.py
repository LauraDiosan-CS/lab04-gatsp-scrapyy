


class Repository:
    def __init__(self):
        self.list = []

    def add(self,c):
        self.list.append(c)

    def delete(self, c):
        self.list.remove(c)

    def findAll(self):
        return self.list

    def get(self,i):
        return self.list[i]

    def sort(self):
        self.list.sort(key = lambda x : x.getFitness(),reverse = False)