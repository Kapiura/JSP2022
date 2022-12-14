import trojkat as tys

#alist = input("Podaj 3 boki trojkata w liscie oddalone spacja")
#a = "".join(alist)
#print(a)
#a=alist[0]
#b=alist[1]
#c=alist[2]
a = int(input("Podaj 1 bok trojkata: "))
b = int(input("Podaj 2 bok trojkata: "))
c = int(input("Podaj 3 bok trojkata: "))
if(c<a+b and b<a+c and a<b+c):   
    print(tys.obwod(a,b,c))
    print(tys.pole(a,b,c))
    print(tys.rrr(a,b,c))
    print(tys.por(a,b,c))
else:
    print("Taki trójkąt nie istnieje")