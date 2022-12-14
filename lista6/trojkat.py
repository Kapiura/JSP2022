import math
def obwod(a,b,c):
    ob = a+b+c
    return ob

def pole(a,b,c):
    p = (a+b+c)/2
    pol = p*(p-a)*(p-b)*(p-c)
    pol = math.sqrt(pol)
    return pol

def rrr(a,b,c):
    if(a==b and a==c):
        return("równoboczny")
    if (a!=b and a!=c and b!=c):
        return("różnoboczny")
    else:
        return("równoramienny")

def por(a,b,c):
    lista = [a,b,c]
    lista.sort()
    a = math.pow(lista[0],2)
    b = math.pow(lista[1],2)
    c = math.pow(lista[2],2)
    ab = a+b
    if(c>ab):
        return("rozwartokątny")
    if(c==ab):
        return("prostokątny")
    if(c<ab):
        return("ostrokątny")    