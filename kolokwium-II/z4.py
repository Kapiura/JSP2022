from datetime import date

class Obywtel():
    def __init__(self,imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        #wzorzec daty ktory wybralem to yyyy-mm-dd
        self.data_urodzenia = data_urodzenia
    def __str__(self):
        rok = int(self.data_urodzenia[:4])
        miesiac = int(self.data_urodzenia[5:7])
        dzien = int(self.data_urodzenia[8:])
        roz_mies = date.today().month - miesiac
        roz_dzien = date.today().day - dzien
        if roz_mies < 0:
            age = date.today().year - rok - 1
        elif roz_mies == 0 and roz_dzien < 0:
            age = date.today().year - rok - 1
        else:
            age = date.today().year - rok
        return f"Obywatelka/ka {self.imie} {self.nazwisko}, wiek {age} lat, urodzony/a {self.data_urodzenia}"

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
data_urodzenia = input("Podaj date urodzenia yyyy-mm-dd: ")
osoba = Obywtel(imie, nazwisko, data_urodzenia)
print(osoba)
