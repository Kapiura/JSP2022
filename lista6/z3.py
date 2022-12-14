def look_and_say(n):
    ciag = "1"
    lista_ciagu = []
    for j in range(n):
        lista_ciagu.append(ciag)
        next = ""
        ile = 1
        for j in range(1, len(ciag)):
            if ciag[j] == ciag[j-1]:
                ile += 1
            else:
                next += str(ile) + ciag[j-1]
                ile = 1
        next += str(ile) + ciag[-1]
        ciag = next
    return lista_ciagu

def wys_ciag(ciag):
    for i in ciag:
        print(i)

a = int(input("podaj n liczbe: "))
print(wys_ciag(look_and_say(a)))