import numpy as np
import sys

cyferki = []

if len(sys.argv) == 1:
    dane = [int(line) for line in sys.stdin]
else:
    dane = sys.argv[1]
    prze = np.array(dane)
    dane = np.char.split(prze,sep=',')
    dane = dane.tolist()
    dane = [eval(i) for i in dane]




def obl(dane):
    s = np.average(dane)
    w = np.var(dane)
    o = np.std(dane)
    print("Srednia : ", s)
    print("Wariancja : ", w)
    print("Odchylenie standardowe : ", o)

obl(dane)