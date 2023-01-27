import itertools as it
test = [1,2,3]


class Klasa():
    def __init__(self,l:list):
        self.lista = l
    def podlisty(self):
        self.lists = []
        for i in range(len(self.lista)+1):
            self.lists += [list(j) for j in it.combinations(self.lista, i)]
        return self.lists

ziut = Klasa(test)
print(ziut.podlisty())