import numpy as np
import matplotlib.pyplot as plt
import math
g = 9.81
vo = int(input("Podaj wartosc poczatkowa v0: "))
kat = int(input("Podaj kąt rzutu w stopniach: "))
#vo = 95
#kat = 50

vyo = np.sin(kat*(np.pi/180))*vo
vxo = np.cos(kat*(np.pi/180))*vo
tw = vyo/g
tc = 2*tw
hmax = vyo*tw-(g*tw**2)/2
z = vxo*tc
print('Maksymalna wysokość rzutu: ',hmax,'\nZasięg rzutu: ',z,'\nCzas lotu: ',tc)

#pr4edkosc chwilowa
plt.subplot(1,3,1)
tcc = np.linspace(0,tc,100)
vx = np.linspace(vxo,vxo,100)
vy = np.abs(vyo-(g*tcc))

plt.title("Wykres prędkości chwilowej")
plt.plot(tcc,vx,label="vx(t)")
plt.plot(tcc,vy,label="vy(t)")
plt.legend()

#polozenie w funkcji czasu

plt.subplot(1,3,2)
Z = vx*tcc
Y = vyo*tcc-((g*tcc**2)/2)
plt.plot(tcc,Z,label='x(t)')
plt.plot(tcc,Y,label='y(t)')
plt.legend()
plt.title('Położenie')

#wykres toru rzutu ukosnego
plt.subplot(1,3,3)
plt.title('Rzut ukośny')
plt.plot(Z,Y,label='y(x)')
plt.legend()

#wyswietlenie wykresow
plt.show()