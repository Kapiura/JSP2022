import math
class Kolo():
    def __init__(self,r):
        self.r = r
    def pole(self):
        return round(math.pi*self.r ** 2,2)
    def obwod(self):
        return round(math.pi*2*self.r)

ziut = Kolo(6)
print(ziut.pole())
print(ziut.obwod())