import datetime
import os
import sys

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




#path = str(input("Podaj ścieżkę do pliku: "))
path = '/home/kapiura/JSP2022/lista8/plik_zaszyfrowany2_2023-01-04.txt'

if os.path.exists(path)!=True:
    print("Błędnie podana ścieżka")
    sys.exit()

#sc = os.system('find plik_zaszyfrowany*')
sc = path.split('/')[-1]
przesuniecie = int(sc.split('_')[1][-1])

try:
    with open(path,'r',encoding='utf-8') as plik:
        temp = plik.read()
        temp_x = deszyfrowanie(temp, przesuniecie)
except:
    print('Błąd')
    sys.exit()
dat = datetime.datetime.now()
new_file_name = 'plik_deszyfrowany'+str(przesuniecie)+'_'+dat.strftime('%Y-%m-%d')+'.txt'

#path = str(input("Podaj ścieżkę do folderu, gdzie chcesz zapisać: "))
path = '/home/kapiura/JSP2022/lista8/'

if os.path.exists(path)!=True:
    os.mkdir(path)
try:
    with open(path+new_file_name,'w',encoding='utf-8') as f:
        f.write(temp_x)
except:
    print("Błąd")