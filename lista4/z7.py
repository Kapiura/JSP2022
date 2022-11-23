def druk(w):
    print(' '.join([str(item) for item in w]))

def pascal(n):
    w = [1]
    druk(w)
    for i in range(int(n) - 1):
        nw = [1]
        for j in range(len(w) - 1):
            nw.append(w[j] + w[j + 1])
        nw.append(1)
        w = nw
        druk(w)
        

n = input("Podaj n ")
pascal(n)