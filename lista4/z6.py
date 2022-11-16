import math
def rnh(r,g,b):
    #dane
    rp = math.degrees(r/255)
    gp = math.degrees(g/255)
    bp = math.degrees(b/255)
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
        h = 60*(((gp-bp)/delta)%6)
    elif(delta!=0 and cmax == gp ):
        h = 60*(((bp-rp)/delta)+2)
    elif(delta!=0 and cmax == bp ):
        h = 60*(((rp-gp)/delta)+4)
    #return wynik
    HSV = list[int(h),int(s*100),int(v*100)]
    return HSV


def hnr(h,s,v):
    c = v*s
    x = c*(1-abs((h/math.degrees(60)%2-1)))
    m = v-c
    if(0<=h<60):
        rp = c
        gp = x
        bp = 0
    elif(60<=h<120):
        rp = x
        gp = c
        bp = 0
    elif(120<=h<180):
        rp = 0
        gp = c
        bp = x
    elif(180<=h<240):
        rp = 0
        gp = x
        bp = c
    elif(240<=h<300):
        rp = x
        gp = 0
        bp = c
    elif(300<=h<360):
        rp = x
        gp = c
        bp = 0
    r = (rp+m)*255
    g = (gp+m)*255
    b = (bp+m)*255
    RGB = list[r,g,b]
    return RGB


wybor = int(input("1.RGB na HSV\n2.HSV na RGB\n"))
if (wybor == 1):
    r = int(input("\nR: "))
    g = int(input("\nG: "))
    b = int(input("\nB: "))
    print(rnh(r,g,b))
elif (wybor == 2):
    s = int(input("\nH: "))
    h = int(input("\nS: "))
    v = int(input("\nV: "))
    print(hnr(h,s,v))