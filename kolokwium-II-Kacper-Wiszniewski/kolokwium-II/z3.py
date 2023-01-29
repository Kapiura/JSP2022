import random
import sortowanie as sor
def generate_list():
    return [random.randint(0, 100) for i in range(1000)]

lista = generate_list()

sor.babelkowe(lista)
sor.wybieranie(lista)
