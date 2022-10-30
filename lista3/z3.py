import cmath as m

print ("ax^2+bx+c=0")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a != 0:
    print("Równanie jest kwadratowe")
    d = (b**2)-(4*a*c)
    print(d)
    if d > 0:
        p = m.sqrt(d)
        x1 = ((-b)+p)/(2*a)
        x2 = ((-b)-p)/(2*a)
        print("Rownanie posiada dwa rozne pierwiastki rzeczywiste: ",x1.real,x2.real)
    elif d == 0:
        x = (-b)/(2*a)
        print("Rownanie posiada dwa takie same pierwiastki rzeczywiste: ",x)
    else:
        print("Rówannie nie posiada pierwiastków rzeczyswitych")
else:
    print("Rownanie nie jest kwadratowe, jest to funkcja liniowa")
    if b != 0:
        x=-c/b
        print("Równanie posiada jedno rozwiązanie rzeczywiste: ",x)
    else:
        if c != 0:
            print("Równanie sprzeczne")
        elif c == 0:
            print("Równanie posiada nieskonczenie wiele rozwiazan")


