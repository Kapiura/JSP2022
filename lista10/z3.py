import itertools as it
test = [5,7,2,1,-3,-5,-1,-2,0,5]


class Klasa():
    def __init__(self,l:list):
        self.lista = l
    def podlisty(self):
        self.lists = []
        self.temp = []
        self.temp += [list(j) for j in it.combinations(self.lista, 3)]
        for k in self.temp:
            if sum(k) == 0:
                self.lists.append(k)
        return self.lists

ziut = Klasa(test)
print(ziut.podlisty())