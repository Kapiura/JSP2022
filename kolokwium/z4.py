wielokrotnosci = [i for i in range(2,100,2)]
for i in range(len(wielokrotnosci)-1):
    if wielokrotnosci[i] % 3 == 0 and wielokrotnosci[i] % 5 != 0:
        print("Syk")
    elif wielokrotnosci[i] % 3 != 0 and wielokrotnosci[i] % 5 == 0:
        print("Bzyk")
    elif  wielokrotnosci[i] % 3 == 0 and wielokrotnosci[i] % 5 == 0:
        print("SykBzyk")
    else:
        print(wielokrotnosci[i])