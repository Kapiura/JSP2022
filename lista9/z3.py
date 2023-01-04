import numpy as np
import matplotlib.pyplot as plt
import math
g = 9.81
#vo = int(input("Podaj wartosc poczatkowa v0: "))
#kat = int(input("Podaj kąt rzutu w stopniach: "))
vo = 95
kat = math.radians(50)
vy = round(vo*math.sin(kat))
vx = round(vo*math.cos(kat))
tw = (vo*math.sin(kat))/g
h = str(vo*tw*math.sin(kat)-(g/2*tw*tw))
z = str((vo*vo/g)*math.sin(2*kat))
tl = str((2*vo*math.sin(kat))/g)
print("Maksymalna wysokość: ",h+' m/s')
print("Zasięg rzutu: ",z+' m')
print("Czas lotu: ",tl+' s')

t = [i for i in range(1,round(float(tl)),1)]

#plot 1 prędkość chwilowa w kierunku pionowym i poziomym po czasie t
y1 = np.array([])
for i in t:
    y1.append(2)

plt.subplot(1, 2, 1)
plt.plot(t,y1)

#plot 2 polozenia w funkcji czasu

#plot 3 wykres rzutu ukosnego


plt.show()