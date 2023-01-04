import datetime
import os
import sys

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




#path = str(input("Podaj ścieżkę do pliku: "))
path = 'payload_338066.txt'

if os.path.exists(path)!=True:
    print("Błędnie podana ścieżka")
    sys.exit()

while(True):\
    #przesuniecie = 2
    przesuniecie = int(input("Podaj od 1-10 przesuniecie: "))
    if przesuniecie >= 1 and przesuniecie <= 10:
        break
        

try:
    with open(path,'r',encoding='utf-8') as plik:
        temp = plik.read()
        temp_x = szyfrowanie(temp,przesuniecie)
except:
    print('Błąd')
    sys.exit()
dat = datetime.datetime.now()
new_file_name = 'plik_zaszyfrowany'+str(przesuniecie)+'_'+dat.strftime('%Y-%m-%d')+'.txt'

#path = str(input("Podaj ścieżkę do folderu, gdzie chcesz zapisać: "))
path = '/home/kapiura/JSP2022/lista8/'

if os.path.exists(path)!=True:
    os.mkdir(path)
try:
    with open(path+new_file_name,'w',encoding='utf-8') as f:
        f.write(temp_x)
except:
    print("Błąd")