import random
mw = [1,3,5,7,8,10,12]
kon = [1,3,7,9]
for k in range(10):
    pesel = []
    #1800-1899 -8
    #1900-1999 -0
    #2000-2099 -2
    #2100-2199 -4
    #2200-2299 -6
    rok = random.randint(1800,2299)

    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        przestepny = True
    else:
        przestepny = False

    miesiac = random.randint(1,12)

    if miesiac in mw:
        dzien = random.randint(1,31)
    elif miesiac == 2:
        if przestepny==True:
            dzien = random.randint(1,28)
        else:
            dzien = random.randint(1,27)
    else:
        dzien = random.randint(1,30)

    pppp = []
    for i in range(4):
        p = str(random.randint(0,9))
        pppp.append(p)

    print(rok,miesiac,dzien,pppp)
    
    if rok >= 1800 and rok<=1899:
        miesiac+=80
    elif rok >= 1900 and rok<=1999:
        miesiac+=0
    elif rok >= 2000 and rok<=2099:
        miesiac+=20
    elif rok >=2100 and rok <= 2199:
        miesiac+=40
    elif rok >= 2200 and rok <= 2299:
        miesiac+=60
    else:
        miesiac = str(miesiac)
        miesiac = list(miesiac)
        temp = miesiac[0]
        miesiac[0]= 0
        miesiac.append(temp)
    if miesiac <10:
        miesiac = str(miesiac)
        miesiac = list(miesiac)
        temp = miesiac[0]
        miesiac[0]= 0
        miesiac.append(temp)

    
    rok = str(rok)
    if type(miesiac)==int:
        miesiac = str(miesiac)
    if dzien < 10:
        dzien = str(dzien)
        dzien = list(dzien)
        temp = dzien[0]
        dzien[0]= 0
        dzien.append(temp)
    else:
        dzien = str(dzien)
    rok = list(rok)
    for i in range(2):
        del rok[0]
    pes=[]
    pes.extend((rok,miesiac,dzien,pppp))
    for i in pes:
        for j in i:
            pesel.append(int(j))

            
    kontrola = sum(pesel[i] * [9, 7, 3, 1][i % 4] for i in range(10)) % 10

    pesel.append(str(kontrola))
    for i in range(len(pesel)-1):
        pesel[i] = str(pesel[i])
    pesel = ''.join(pesel)
    print(pesel)
    with open('PESEL.txt','a') as plik:
        plik.write(pesel+'\n')
