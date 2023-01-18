
test = [1,2,3]


class Klasa():
    def __init__(self,l):
        self.lista = l
    def podlisty(self):
        podlisty = []
        #appending sublists
        for i in range(0,len(self.lista)):
            for j in range(len(self.lista)):
                    podlisty.append(self.lista[i:i+j])

        # #deleting duplicates
        # for b in podlisty:
        #     i = len(podlisty)-1
        #     czy = 0
        #     temp = b
        #     while i >= 0:
        #         if czy != 0 and podlisty[i]==temp:
        #             podlisty.remove(podlisty[i])
        #         if podlisty[i] == temp:
        #             czy = 1
        #         i-=1

        
        return podlisty

ziut = Klasa(test)
print(ziut.podlisty())

len=3
i = 0
j = 0
[]
i=0
j=1
[1]
i=0
j=2
[1,2]
i=0
j=3
[1,2,3]
