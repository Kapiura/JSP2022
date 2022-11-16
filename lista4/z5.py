

def permutuj(lista, poz = 0):
    dl = len(lista)
    if (poz == len(lista)):
        print(lista)
    else:
        for i in range(poz, dl):
            lista[i], lista[poz] = lista[poz], lista[i]
            permutuj(lista, poz + 1)
            lista[i], lista[poz] = lista[poz], lista[i]


lista = [1,2]
permutuj(lista)