from time import perf_counter

def iteracyjnie(n):
    start  = perf_counter()
    a1 = 0
    a2 = 1
    for i in range(n):
        if i == 0  or i == 1:
            print(i)
        else:
            a3 = a2 + a1
            print(a3)
            a1 = a2
            a2 = a3
    koniec = perf_counter()
    czas = koniec-start
    print("Iteracyjnie zajęło to: ", '{:0.10f}'.format(czas),'s')

def rekurencyjnie(n):
    if n == 0 or n ==1:
        return n
    else:
        return rekurencyjnie(n-1) + rekurencyjnie(n-2)

def wypisanie_rekurencyjnie(n):
    start  = perf_counter()
    for i in range(n):
        print(rekurencyjnie(i))
    koniec = perf_counter()
    czas = koniec-start
    print("Rekurencyjnie zajęło to: ", '{:0.10f}'.format(czas),'s')


n = int(input("podaj n liczbe a wypisze od 0 do n wyrazu ciagu fibonacciego: "))
iteracyjnie(n)
wypisanie_rekurencyjnie(n)