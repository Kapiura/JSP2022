def zad(n, a1, q):
    if (n == 1):
        return a1
    else:
        wynik = a1*(q**(n-1))
        return wynik
n = int(input("Podaj n : "))
a1 = 1
q = 2
print(zad(n,a1,q))