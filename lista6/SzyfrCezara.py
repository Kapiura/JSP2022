def szyfrowanie(txt,kry):
    newtxt = ""
    for i in range(len(txt)):
        liczba = ord(txt[i])
        if liczba >=65 and liczba <=90:
            if liczba + kry > 90:
                newtxt += chr(liczba+kry-26)
            else:
                newtxt += chr(liczba+kry)
        elif liczba >=97 and liczba <= 122:
            if liczba + kry > 122:
                newtxt += chr(liczba+kry-26)
            else:
                newtxt += chr(liczba+kry)
        else:
            newtxt += chr(liczba)
    return newtxt




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

