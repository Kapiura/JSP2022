klucz = {
    'a' : 'y',
    'e' : 'i',
    'i' : 'o',
    'o' : 'a',
    'y' : 'e'
    }
def szyfrowanie(slowo):
    a = slowo
    a = a.split()
    slowo = slowo.split()
    for i in range(len(slowo)):
        sl = slowo[i]
        slowo[i] = list(sl)
    for i in range(len(a)):
        sl = slowo[i]
        a[i] = list(sl)
    for dv, v in klucz.items():
        for i in range(len(slowo)):
            for j in range(len(slowo[i])):
                if slowo[i][j] == dv and slowo[i][j] == a[i][j]:
                    slowo[i][j] = v
    for i in range(len(slowo)):
        slowo[i] = "".join(slowo[i])
        a[i] = "".join(a[i])
    slowo = str(' '.join(slowo))
    return(slowo)

def deszyfrowanie(slowo):
    a = slowo
    a = a.split()
    slowo = slowo.split()
    for i in range(len(slowo)):
        sl = slowo[i]
        slowo[i] = list(sl)
    for i in range(len(a)):
        sl = slowo[i]
        a[i] = list(sl)
    for v, dv in klucz.items():
        for i in range(len(slowo)):
            for j in range(len(slowo[i])):
                if slowo[i][j] == dv and slowo[i][j] == a[i][j]:
                    slowo[i][j] = v
    for i in range(len(slowo)):
        slowo[i] = "".join(slowo[i])
        a[i] = "".join(a[i])
    slowo = str(' '.join(slowo))
    return(slowo)


a = "to jest moj tekst"
print(szyfrowanie(a))
print(deszyfrowanie(szyfrowanie(a)))
txt = input("Podaj zdanie a je zaszyfruje i odszyfruje: ")
print(szyfrowanie(a))
print(deszyfrowanie(szyfrowanie(txt)))
