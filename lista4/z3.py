import math
 

def knr(w):
    radiany = (w*math.pi)/180
    return radiany

def rnk(w):
    katy = (w*180)/math.pi
    return katy

wybor = int(input("1. Zamiana kata na radiany \n2. Zamiana radiana na katy\n"))

kr = float(input("Podaj wartosc : "))

if (wybor == 1):
    print(knr(kr))
elif(wybor == 2):
    print(rnk(kr))