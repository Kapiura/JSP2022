import SzyfrCezara as sc

txt = input("Napisz zdanie jakies a je zakoduje szyfrem cezara ")
a = int(input("Podaj klucz(liczbę) "))
print("Pierwotny teskt: ",txt)
ztxt = sc.szyfrowanie(txt,a)
dtxt = sc.deszyfrowanie(ztxt,a)
print(txt)
print("To twoje zaszyfrowane zdanie: ",ztxt)
print("A tak wygląda po deszyfrowaniu: ",dtxt)