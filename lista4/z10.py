def NWD(a,b):
    while True:
        x = a%b
        if x == 0:
            print(b)
            break
        else:
            a = b
            b = x

NWD(282,78)