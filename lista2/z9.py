from itertools import chain

numbers = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

print(numbers)
l = len(numbers)

def f(x, lista):
    lista = list(chain(lista[x]))

#numbers = list(*chain(x) for x in numbers)
#x=0
#numbers = list(chain(numbers[(x for x in range(l))]))

print(f(0,numbers))

print(numbers)