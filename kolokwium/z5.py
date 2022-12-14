samogloski = ['a','ą','e','ę','i','o','ó','u','y']


def pierwszakropka(slowo):
    s = 2
    slowo = str(slowo)
    slowo = slowo.lower()
    for i in slowo:
        for j in samogloski:
            if i == j:
                s+=1
    if s % 2 == 0:
        return 2
    else:
        return 1


print(pierwszakropka('Ala'))
print(pierwszakropka('ma'))


def drugakropka(tekst):
    s = 0
    suma = 0
    tekst = str(tekst)
    tekst = tekst.lower()
    tekst = list(tekst.split(' '))
    for wyraz in tekst:
        for literka in wyraz:
            for j in samogloski:
                if literka == j:
                    s+=1
        if s % 2 == 0:
            suma+=2
            s= 0
        else:
            suma+=1
            s=0
    return suma


print(drugakropka('Ala ma kota'))


def trzeciakropka(tekstUser):
    s = 0
    suma = 0
    tekstUser = str(tekstUser)
    tekstUser = tekstUser.lower()
    tekstUser = list(tekstUser.split(' '))
    for wyraz in tekstUser:
        for literka in wyraz:
            for j in samogloski:
                if literka == j:
                    s+=1
        if s % 2 == 0:
            suma+=2
            s= 0
        else:
            suma+=1
            s=0
    return suma

userText = str(input("Podaj teskt a ja policze zdobyte przez Ciebie punkty: "))
print(trzeciakropka(userText))
