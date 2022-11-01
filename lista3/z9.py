n = int(input("Wprowadz liczbe kolumn: "))
m = int(input("Wprowadz liczbe wierszy: "))


for i in range(m):
    for j in range(n):
        print(i*j, end="\t")
    print()
