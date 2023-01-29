import sys
def dzielniki(x):
    ld = []
    for i in range(x):
        if x % (x-i) == 0:
            ld.append(x-i)
    return ld

def pierwsza(x):
    dana = dzielniki(x)
    if len(dana)==2:
        return True
    else:
        return False

def doskonala(x):
    dana = dzielniki(x)
    dana.remove(x)
    suma = 0
    for i in dana:
        suma+=i
    if suma==x:
        return True
    else:
        return False
try:
    x = int(input("Podaj liczbe: "))
except:
    sys.exit()
try:
    if x<0:
        raise ValueError
except:
    sys.exit()

print("Dzielniki liczby ",x," to: ",dzielniki(x))
if pierwsza(x):
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
if doskonala(x):
    print("Liczba jest doskonala")
else:
    print("Liczba nie jest doskonala")
