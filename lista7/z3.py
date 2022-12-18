import random
from time import perf_counter

def generatorLiczb():
    losoweListy = []
    b = 100
    for i in range(3):
        newList = []
        for j in range(b):
            n = random.randint(0,20)
            newList.append(n)
        losoweListy.append(newList)
        b+=100
    return losoweListy

def wypisz(lista, czas):
    print('lista z ',len(lista),' elemenatami')
    print(lista)
    print("Sortowanie tej listy zajęło to: ", '{:0.10f}'.format(czas),'s')
    print('')


def sortingLista(lista):
    start  = perf_counter()
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j-1]>lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
    koniec = perf_counter()
    czas = koniec-start
    wypisz(lista,czas)
    return lista


def sortuj(lista):
    for i in lista:
        sortingLista(i)

los = generatorLiczb()
for i in los:
    print('lista z ',len(i),' elemenatami')
    print(i)
    print('')

sortuj(los)