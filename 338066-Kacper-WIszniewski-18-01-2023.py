import numpy as np
class Zepspolona:
    def __init__(self,re,im):
        self.re = re
        self.im = im
    def modul(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5
    def argument(self):
        return np.arctan(self.im/self.re)
    @staticmethod
    def dodaj(z1,z2):
        return z1.re + z1.im + z2.re + z2.im
    def odejmij(z1,z2):
        return (z1.re + z1.im)- (z2.re + z2.im)
    def mnoz(z1,z2):
        return (z1.re +z1.im)*(z2.re + z2.im)
    def dziel(z1,z2):
        return (z1.re + z1.im) / (z2.re + z1.im)
    

        
z = Zepspolona(2,5j)
z2 = Zepspolona(1,1j)
print(Zepspolona.dodaj(z,z2))
print(Zepspolona.odejmij(z,z2))
print(Zepspolona.mnoz(z,z2))
print(Zepspolona.dziel(z,z2))
print(z.modul())
print(z.argument())