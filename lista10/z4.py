from bs4 import BeautifulSoup as bs
import os

class Przelicznik_walut:
    def __init__(self,path):
        self.path = path
        with open(path, 'rb') as f_in:
            self.xml_soup = bs(f_in.read(), 'xml')
        self.kursy = {}
        for i in self.xml_soup.find_all('pozycja'):
            self.kursy[i.kod_waluty.string] = float(i.kurs_sredni.string.replace(',','.'))
    def wyswietl_kursy(self):
        for i in self.kursy:
            print(i, self.kursy[i])
    def przelicz_pln_na_inna(self,kwota,waluta):
        es = str(round(kwota/self.kursy[waluta],2))+' '+waluta
        return es
    def przelicz_inna_na_pln(self,kwota,waluta):
        es = str(round(kwota*self.kursy[waluta],2))+' PLN'
        return es
    def przelicz_inna_na_inna(self,kwota,waluta,waluta2):
        es = str(round(kwota*self.kursy[waluta]/self.kursy[waluta2],2))+' '+waluta2
        return es

        


def wybor():
    print('\n1. Wyswietl kurs walut\n2. Konwersja z pln na wybrana walute i na odwrot\n3. Konwersja wybranej waluty na inna wybrana walute\n')

if __name__ == '__main__':
    os.system('clear')
    p = Przelicznik_walut('/home/kapiura/JSP2022/lista10/kursy.xml')
    while(True):
        wybor()
        wyr = int(input("Wybierz instrukcje: "))
        match wyr:
            case 1 :
                os.system('clear')
                p.wyswietl_kursy()
            case 2:
                wyr2 = int(input('1. Pln na inna\n2. Inna na pln: '))
                match wyr2:
                    case 1:
                        os.system('clear')
                        kwota = int(input('Podaj kwote: '))
                        waluta = str(input('Podaj walute: '))
                        print(p.przelicz_pln_na_inna(kwota,waluta))
                    case 2:
                        os.system('clear')
                        kwota = int(input('Podaj kwote: '))
                        waluta = str(input('Podaj walute: '))
                        print(p.przelicz_inna_na_pln(kwota,waluta))
                    case _:
                        os.system('clear')
                        print('Nie ma takiej instrukcji')
                        break
            case 3:
                os.system('clear')
                kwota = int(input('Podaj kwote: '))
                waluta = str(input('Podaj walute: '))
                waluta2 = str(input('Podaj walute: '))
                print(p.przelicz_inna_na_inna(kwota,waluta,waluta2))
            case _:
                print('Nie ma takiej instrukcji')
                break
