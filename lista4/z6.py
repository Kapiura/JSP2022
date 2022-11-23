import math
def rnh(r,g,b):
    #dane
    rp = r/255
    gp = g/255
    bp = b/255
    cmax = max(rp, gp, bp)
    cmin = min(rp, gp, bp)
    delta = cmax - cmin
    #V
    v = cmax
    #S
    if (cmax == 0):
        s = 0
    elif (cmax!= 0):
        s = delta/cmax
    #H
    if(delta == 0):
        h = 0
    elif(delta!=0 and cmax == rp ):
        h = 60*(((gp-bp)/delta)%6)%360
    elif(delta!=0 and cmax == gp ):
        h = 60*(((bp-rp)/delta)+2)%360
    elif(delta!=0 and cmax == bp ):
        h = 60*(((rp-gp)/delta)+4)%360
    #return wynik
    print("H-",round(h),"S-",round(s*100),"V-",round(v*100), sep=" ")


def hnr(h,s,v):
    h%=360
    s /= 100
    v /= 100
    if 0 <= h < 360 and 0 <= s <= 1 and 0 <= v <= 1:
        c = s * v
        x = c * (1 - ((h / 60) % 2 - 1))
        m = v - c

    if 0 <= h < 60:
        rp = c
        gp = x
        bp = 0
    elif 60 <= h < 120:
        rp = x
        gp = c
        bp = 0
    elif 120 <= h < 180:
        rp = 0
        gp = c
        bp = x
    elif 180 <= h < 240:
        rp = 0
        gp = x
        bp = c
    elif 240 <= h < 300:
        rp = x
        gp = 0
        bp = c
    elif 300 <= h < 360:
        rp = c
        gp = 0
        bp = x

    r = round((rp + m) * 255)
    g = round((gp + m) * 255)
    b = round((bp + m) * 255)
    print (r, g, b)

wybor = int(input("1.RGB na HSV\n2.HSV na RGB\n"))
if (wybor == 1):
    r = int(input("\nR: "))
    g = int(input("\nG: "))
    b = int(input("\nB: "))
    rnh(r,g,b)
elif (wybor == 2):
    h = int(input("\nH: "))
    s = int(input("\nS: "))
    v = int(input("\nV: "))
    hnr(h,s,v)