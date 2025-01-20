from time import perf_counter


def babelkowe(lista):
    start  = perf_counter()
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j-1]>lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
    koniec = perf_counter()
    czas = koniec-start
    print("Sortowanie tej listy bąbelkowo zajęło: ", '{:0.10f}'.format(czas),'s')
    return lista

def wybieranie(lista):
    start  = perf_counter()
    for i in range(len(lista)-1):
        min = i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[min]:
                min = j
        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp
    koniec = perf_counter()
    czas = koniec-start
    print("Sortowanie tej listy wybieraniem zajęło: ", '{:0.10f}'.format(czas),'s')
    return lista

