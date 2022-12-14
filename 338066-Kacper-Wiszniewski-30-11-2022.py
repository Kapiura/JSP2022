#Kacper Wiszniewski 338066
#napisz funkcje ktora bierze sekwencje s = "GTACAGTA"
#pozamienieac literki
# A -> T
# C -> G
# T -> A
# G -> C
#senkwencje i nalezy do klucza

klucz = {
    'A' : 'T',
    'C' : 'G',
    'T' : 'A',
    'G' : 'C'
}


def DNA(slowo):
    a = slowo
    a = a.split()
    slowo = slowo.split()
    for dv,v in klucz.items():
        if slowo in klucz.items():
            return("Błędnie podana sekwencja")
        else:     
            for i in range(len(slowo)):
                sl = slowo[i]
                slowo[i] = list(sl)
            for i in range(len(a)):
                sl = slowo[i]
                a[i] = list(sl)
            for dv, v in klucz.items():
                for i in range(len(slowo)):
                    for j in range(len(slowo[i])):
                        if slowo[i][j] == dv and slowo[i][j] == a[i][j]:
                            slowo[i][j] = v
            for i in range(len(slowo)):
                slowo[i] = "".join(slowo[i])
                a[i] = "".join(a[i])
            slowo = str(' '.join(slowo))
            return(slowo)
        

sd = "GTACAGTA"
print(DNA(sd))
inne = input("Podaj własną sekwencje: ")
print(DNA(inne))