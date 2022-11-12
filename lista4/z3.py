import math

def knr(w):
    w = int(input("Podaj kąt w stopniach"))
    radiany = (w*math.pi)/180
    return radiany

def rnk(w):
    w = int(input("Podaj kąt w radianach"))
    katy = (w*180)/math.pi
    return katy

wybor = input("1. Zamiana kata na radiany \n2. Zamiana radiana na katy\n")

while(wybor!="0" or wybor!="1"):
    wybor = input("1. Zamiana kata na radiany \n2. Zamiana radiana na katy\n")
    if wybor!="0" or wybor!="1":
        print("Wpisz poprawne wartosci!")
kr = float(input("Podaj wartosc"))

