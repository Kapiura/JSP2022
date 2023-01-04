from time import perf_counter


def deszyfrowanie(txt, kry):
    newtxt = ""
    for i in range(len(txt)):
        liczba = ord(txt[i])
        if liczba >=65 and liczba <=90:
            if liczba - kry < 65:
                newtxt += chr(liczba-kry+26)
            else:
                newtxt += chr(liczba-kry)
        elif liczba >=97 and liczba <= 122:
            if liczba - kry < 97:
                newtxt += chr(liczba-kry+26)
            else:
                newtxt += chr(liczba-kry)
        else:
            newtxt += chr(liczba)
    return newtxt


start  = perf_counter()
x = [i for i in range(1,26,1)]
with open('payload_338066.txt','r',encoding='utf-8') as plik:
    temp = plik.read()
    for i in x:
        temp_d = str(deszyfrowanie(temp,i))
        if 'Kacper' in temp_d:
            if 'Wiszniewski' in temp_d:
                if '338066' in temp_d:
                    print(temp_d)
                    with open('hacked_338066.txt', 'w',encoding='utf-8') as f:
                        f.write(temp_d)
                        f.close()
                    break
    plik.close()
koniec = perf_counter()
print(koniec-start)