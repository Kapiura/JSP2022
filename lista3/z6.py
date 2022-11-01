q = int(input("Wprowadz liczbe: "))
w = (1,2,...,10)
r = (1,2,...,q)


print("\t", end="")


for i in range(q):
    i+=1
    print(i, end="\t")
print()
for j in range(10):
    j+=1
    print(j, end="\t")
    for k in range(q):
        k+=1
        print(k*j, end="\t")
    print()
