#napisz funkcje ktora w tekscie zastapi wszystkie nazwiska ich pierwsza litera i kropka
#Nowak = N.
#lista nazwisk Nowak Kowalski Kowal
#tekst adam kowal i marek nowak zostali skazani
#funkcja bierze napis i zmienia napis 
def lts(s):
    sd = " "
    return (sd.join(s))

def zmiana(zdanie):
    nazwiska = ["Nowak","Kowalski","Kowal"]
    nazzmiana = ["N.","K.","K."]
    listazdania = zdanie.split()
    dl = len(listazdania)
    i=0
    while(i < dl):
        if (listazdania[i]==nazwiska[0]):
            listazdania[i]=nazzmiana[0]
        elif(listazdania[i]==nazwiska[1]):
            listazdania[i]=nazzmiana[1]
        elif(listazdania[i]==nazwiska[2]):
            listazdania[i]=nazzmiana[2]
        i+=1
    zdanie = lts(listazdania)
    return zdanie
    


tekst = "Adam Kowal i Marek Nowak zostali skazani"
print(tekst)
print(zmiana(tekst))