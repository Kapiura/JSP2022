liczby = [i for i in range(1,6,1)]
suma = 0
iloczyn = 1
print(liczby)
for s in range(len(liczby)):
    suma+=liczby[s]
print("Suma wynosi: ",suma)
for i in range(len(liczby)):
    iloczyn*=liczby[i]
print("Iloczyn wynosi", iloczyn)
    