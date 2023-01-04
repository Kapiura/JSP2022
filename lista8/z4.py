import sys
try:
    with open('PESEL.txt','r') as plik:
        for line in plik:
            line = line.strip()
            #line = list(line)
            print(line)
            kontrola = sum(int(line[i]) * [9, 7, 3, 1][i % 4] for i in range(10)) % 10
            if int(line[-1]) == int(kontrola):
                rok = int(line[0:2])
                miesiac = int(line[2:4])
                dzien = int(line[4:6])
                if miesiac > 80:
                    rok+=1800
                    miesiac-=80
                elif miesiac > 60:
                    rok+=2200
                    miesiac-=60
                elif miesiac > 40:
                    rok+=2100
                    miesiac-=40
                elif miesiac > 20:
                    rok+=2000
                    miesiac-=20
                else: 
                    rok+=1900
                if int(line[-2]) % 2:
                    plec = 'kobieta'
                else:
                    plec = 'mezczyzna'
                with open('PESEL-odczytany.txt','a') as file:
                    ziut = str(line)+':\ndata urodzenia '+str(dzien)+'-'+str(miesiac)+'-'+str(rok)+'\t płeć: '+plec+'\n'
                    file.write(ziut)

except:
    print('Błąd')
    sys.exit()