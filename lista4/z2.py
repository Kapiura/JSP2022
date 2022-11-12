def ziut(l):
    l = list(l)
    print(l)
    print("Usuwanie duplikatow")
    l = list(dict.fromkeys(l))
    print(l)

lista = [9,9,6]
ziut(lista)